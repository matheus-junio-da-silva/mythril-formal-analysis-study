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
from pathlib import Path
from mythril.mythril import MythrilDisassembler


def test_custom_jumpdest():

    time_handler.start_execution(30)  # 30 seconds
    """
    -------->>>>>> codigo para obter bytecode <<<<<<--------
    
    # Cria o disassembler com a versão do solc desejada
    disassembler = MythrilDisassembler(eth=None, solc_version="v0.4.25")

    # Como o contrato FunctionTypes.sol está no mesmo diretório deste arquivo,
    # usamos __file__ para obter o caminho atual.
    contract_path = str(Path(__file__).resolve().parent / "FunctionTypes.sol")

    # Carrega o contrato Solidity e obtém o bytecode
    address, contracts = disassembler.load_from_solidity([contract_path])

    code = contracts[0].code

    print("Address:", address)
    print("Bytecode:", code)
    """
    address = "0x0000000000000000000000000000000000000000"
    bytecode = "608060405260043610610041576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680636a1f9e1914610046575b600080fd5b61004e610050565b005b6100586101ee565b600034141515156100d1576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600b8152602001807f73656e642066756e64732100000000000000000000000000000000000000000081525060200191505060405180910390fd5b61010c816000019067ffffffffffffffff16908167ffffffffffffffff1681525050348151018152610109816000015163ffffffff16565b50565b610114610116565b565b60003414151561018e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260108152602001807f646f6e742073656e642066756e6473210000000000000000000000000000000081525060200191505060405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f193505050501580156101eb573d6000803e3d6000fd5b50565b60206040519081016040528061020381525090565bfe00a165627a7a72305820fa71826a20e612e65a779fe04f6cf1ddaf34474bb93cd67dd6bd6d5635caf4330029"

    print("Address:", address)
    print("Bytecode:", bytecode)

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
    # cada elemento pode ser um valor concreto ou um valor simbólico (geralmente representado por BitVec)
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