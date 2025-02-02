from mythril.analysis.module.modules.arbitrary_jump import ArbitraryJump
from mythril.laser.ethereum.state.machine_state import MachineStack, MachineState
from mythril.laser.smt import BitVec, Concat, Extract, symbol_factory
from mythril.laser.ethereum.state.global_state import GlobalState
from mythril.disassembler.disassembly import Disassembly
from mythril.laser.ethereum.state.account import Account
from mythril.laser.ethereum.state.environment import Environment
from mythril.laser.ethereum.state.world_state import WorldState
from mythril.laser.ethereum.transaction.transaction_models import MessageCallTransaction
from mythril.laser.ethereum.call import SymbolicCalldata
from mythril.laser.ethereum.transaction.symbolic import ACTORS
from mythril.laser.ethereum.time_handler import time_handler

def test_custom_jumpdest():

    time_handler.start_execution(30)  # 30 seconds

    # Configuração básica do WorldState
    world_state = WorldState()
    
    # Configuração da conta
    active_account = Account("0x0", code=Disassembly("60606040"))  # Código de exemplo: PUSH1 0x40
    
    # Contexto da transação (remetente, dados, gás, etc.)
    environment = Environment(
        active_account=active_account,
        sender=ACTORS.attacker,  
        calldata=SymbolicCalldata("2"),
        gasprice=symbol_factory.BitVecVal(0, 256),  
        callvalue=symbol_factory.BitVecVal(0, 256),  
        origin=ACTORS.attacker,
        basefee=symbol_factory.BitVecVal(0, 256),
        code=active_account.code
    )
    
    # Estado da EVM durante a execução (stack, memória, PC, etc.)
    machine_state = MachineState(gas_limit=8000000)
    
    # Transação simbólica que será executada      
    transaction = MessageCallTransaction(
        world_state=world_state,
        gas_limit=8000000,
        caller=ACTORS.attacker,
        callee_account=active_account,
        call_value=symbol_factory.BitVecSym("call_value", 256)
    )
    
    # Configuração do GlobalState
    state = GlobalState(
        world_state=world_state,
        environment=environment,
        machine_state=machine_state,
        node=None
    )
    
    # Adiciona a transação à sequência
    state.world_state.transaction_sequence = [transaction]
    
    # Criação da stack personalizada
    # Variável simbólica que representa um valor controlado pelo usuário (ex: msg.value).
    call_value2 = symbol_factory.BitVecSym("call_value2", 256)
    
    # Valor construído para simular o destino do salto
    raw_value = Concat(
        symbol_factory.BitVecVal(0, 8), #Cria um valor de 8 bits com todos os bits definidos como 0
        Extract(31, 8, symbol_factory.BitVecVal(268, 256) + call_value2), # Extrai 8 bits (do bit 31 ao bit 24) do valor resultante da soma de 268 e call_value2
        Extract(7, 0, call_value2) + symbol_factory.BitVecVal(12, 8) # Extrai os 8 bits menos significativos (do bit 7 ao bit 0) de call_value2
    )
    
    # Configuração da stack
    state.mstate.stack = [raw_value]
    
    # Adição de constraints
    # call_value2 terá apenas um valor possível -> sem vulnerabilidade
    #state.world_state.constraints.append(call_value2 == symbol_factory.BitVecVal(0x1234, 256))

    # Execução do detector
    detector = ArbitraryJump()
    issues = detector._analyze_state(state)
    
    print(f"Vulnerabilidades encontradas: {len(issues)}")
    # Imprimindo detalhes das issues
    for idx, issue in enumerate(issues, start=1):
        print(f"\n--- Vulnerabilidade {idx} ---")
        print(f"Título: {issue.title}")
        print(f"Contrato: {issue.contract}")
        #print(f"Função: {issue.function_name}")
        print(f"Endereço: {issue.address}")
        print(f"SWC ID: {issue.swc_id}")
        print(f"Severidade: {issue.severity}")
        print(f"Descrição: {issue.description_head} {issue.description_tail}")
        #print(f"Bytecode: {issue.bytecode}")
        print(f"Sequência de Transações: {issue.transaction_sequence}")
        print("---------------------------\n")

test_custom_jumpdest()