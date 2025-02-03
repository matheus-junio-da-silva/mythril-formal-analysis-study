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
"""
    ao verificar as instrucoes do mythril,
    devemos tomar cuidado com a ordem das instrucoes
    que sao verificadas, pois ele utiliza Depth-First Search (DFS) 
    com prioridade de estados ativos
    ex:
    address: 100 (Bloco 1)
    address: 209 (Bloco 2)
    address: 102 (Bloco 1)
    address: 210 (Bloco 2)
    ...
    Isso mostra que o Mythril está alternando 
    entre dois estados ativos (um para cada bloco).
"""

"""
    O destino do salto (JUMPDEST) é calculado dinamicamente 
    (provavelmente usando MLOAD/CALLVALUE).

    Se o destino for controlado por um usuário 
    (ex: via calldata), é uma vulnerabilidade SWC-127.
"""

"""
    parte vulnerável do contrato:

    assembly { 
        mstore(func, add(mload(func), callvalue)) 
    }

    Funcionamento:

    -> mload(func): Lê o valor armazenado no endereço 
    de memória de func.

    -> add(..., callvalue): Soma callvalue 
    (valor enviado na transação) ao valor lido.

    -> mstore(func, ...): Escreve o novo valor de 
    volta no endereço de func.

"""
"""

"""


def test_custom_jumpdest():
    

    time_handler.start_execution(30)  # 30 seconds
    
    #-------->>>>>> codigo para obter bytecode <<<<<<--------
    
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
    print(contracts[0].disassembly.instruction_list)

    address = "0x0000000000000000000000000000000000000000"
    bytecode = "608060405260043610610041576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680636a1f9e1914610046575b600080fd5b61004e610050565b005b6100586101ee565b600034141515156100d1576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600b8152602001807f73656e642066756e64732100000000000000000000000000000000000000000081525060200191505060405180910390fd5b61010c816000019067ffffffffffffffff16908167ffffffffffffffff1681525050348151018152610109816000015163ffffffff16565b50565b610114610116565b565b60003414151561018e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260108152602001807f646f6e742073656e642066756e6473210000000000000000000000000000000081525060200191505060405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f193505050501580156101eb573d6000803e3d6000fd5b50565b60206040519081016040528061020381525090565bfe00a165627a7a72305820fa71826a20e612e65a779fe04f6cf1ddaf34474bb93cd67dd6bd6d5635caf4330029"
    # instrucoes que vao do comeco ate o jump vulneravel
    instructions = [{'address': 0, 'opcode': 'PUSH1', 'argument': '0x80'}, {'address': 2, 'opcode': 'PUSH1', 'argument': '0x40'}, {'address': 4, 'opcode': 'MSTORE'}, {'address': 5, 'opcode': 'PUSH1', 'argument': '0x04'}, {'address': 7, 'opcode': 'CALLDATASIZE'}, {'address': 8, 'opcode': 'LT'}, {'address': 9, 'opcode': 'PUSH2', 'argument': '0x0041'}, {'address': 12, 'opcode': 'JUMPI'}, {'address': 13, 'opcode': 'PUSH1', 'argument': '0x00'}, {'address': 15, 'opcode': 'CALLDATALOAD'}, {'address': 16, 'opcode': 'PUSH29', 'argument': '0x0100000000000000000000000000000000000000000000000000000000'}, {'address': 46, 'opcode': 'SWAP1'}, {'address': 47, 'opcode': 'DIV'}, {'address': 48, 'opcode': 'PUSH4', 'argument': '0xffffffff'}, {'address': 53, 'opcode': 'AND'}, {'address': 54, 'opcode': 'DUP1'}, {'address': 55, 'opcode': 'PUSH4', 'argument': '0x6a1f9e19'}, {'address': 60, 'opcode': 'EQ'}, {'address': 61, 'opcode': 'PUSH2', 'argument': '0x0046'}, {'address': 64, 'opcode': 'JUMPI'}, {'address': 65, 'opcode': 'JUMPDEST'}, {'address': 66, 'opcode': 'PUSH1', 'argument': '0x00'}, {'address': 68, 'opcode': 'DUP1'}, {'address': 69, 'opcode': 'REVERT'}, {'address': 70, 'opcode': 'JUMPDEST'}, {'address': 71, 'opcode': 'PUSH2', 'argument': '0x004e'}, {'address': 74, 'opcode': 'PUSH2', 'argument': '0x0050'}, {'address': 77, 'opcode': 'JUMP'}, {'address': 78, 'opcode': 'JUMPDEST'}, {'address': 79, 'opcode': 'STOP'}, {'address': 80, 'opcode': 'JUMPDEST'}, {'address': 81, 'opcode': 'PUSH2', 'argument': '0x0058'}, {'address': 84, 'opcode': 'PUSH2', 'argument': '0x01ee'}, {'address': 87, 'opcode': 'JUMP'}, {'address': 88, 'opcode': 'JUMPDEST'}, {'address': 89, 'opcode': 'PUSH1', 'argument': '0x00'}, {'address': 91, 'opcode': 'CALLVALUE'}, {'address': 92, 'opcode': 'EQ'}, {'address': 93, 'opcode': 'ISZERO'}, {'address': 94, 'opcode': 'ISZERO'}, {'address': 95, 'opcode': 'ISZERO'}, {'address': 96, 'opcode': 'PUSH2', 'argument': '0x00d1'}, {'address': 99, 'opcode': 'JUMPI'}, {'address': 100, 'opcode': 'PUSH1', 'argument': '0x40'}, {'address': 102, 'opcode': 'MLOAD'}, {'address': 103, 'opcode': 'PUSH32', 'argument': '0x08c379a000000000000000000000000000000000000000000000000000000000'}, {'address': 136, 'opcode': 'DUP2'}, {'address': 137, 'opcode': 'MSTORE'}, {'address': 138, 'opcode': 'PUSH1', 'argument': '0x04'}, {'address': 140, 'opcode': 'ADD'}, {'address': 141, 'opcode': 'DUP1'}, {'address': 142, 'opcode': 'DUP1'}, {'address': 143, 'opcode': 'PUSH1', 'argument': '0x20'}, {'address': 145, 'opcode': 'ADD'}, {'address': 146, 'opcode': 'DUP3'}, {'address': 147, 'opcode': 'DUP2'}, {'address': 148, 'opcode': 'SUB'}, {'address': 149, 'opcode': 'DUP3'}, {'address': 150, 'opcode': 'MSTORE'}, {'address': 151, 'opcode': 'PUSH1', 'argument': '0x0b'}, {'address': 153, 'opcode': 'DUP2'}, {'address': 154, 'opcode': 'MSTORE'}, {'address': 155, 'opcode': 'PUSH1', 'argument': '0x20'}, {'address': 157, 'opcode': 'ADD'}, {'address': 158, 'opcode': 'DUP1'}, {'address': 159, 'opcode': 'PUSH32', 'argument': '0x73656e642066756e647321000000000000000000000000000000000000000000'}, {'address': 192, 'opcode': 'DUP2'}, {'address': 193, 'opcode': 'MSTORE'}, {'address': 194, 'opcode': 'POP'}, {'address': 195, 'opcode': 'PUSH1', 'argument': '0x20'}, {'address': 197, 'opcode': 'ADD'}, {'address': 198, 'opcode': 'SWAP2'}, {'address': 199, 'opcode': 'POP'}, {'address': 200, 'opcode': 'POP'}, {'address': 201, 'opcode': 'PUSH1', 'argument': '0x40'}, {'address': 203, 'opcode': 'MLOAD'}, {'address': 204, 'opcode': 'DUP1'}, {'address': 205, 'opcode': 'SWAP2'}, {'address': 206, 'opcode': 'SUB'}, {'address': 207, 'opcode': 'SWAP1'}, {'address': 208, 'opcode': 'REVERT'}, {'address': 209, 'opcode': 'JUMPDEST'}, {'address': 210, 'opcode': 'PUSH2', 'argument': '0x010c'}, {'address': 213, 'opcode': 'DUP2'}, {'address': 214, 'opcode': 'PUSH1', 'argument': '0x00'}, {'address': 216, 'opcode': 'ADD'}, {'address': 217, 'opcode': 'SWAP1'}, {'address': 218, 'opcode': 'PUSH8', 'argument': '0xffffffffffffffff'}, {'address': 227, 'opcode': 'AND'}, {'address': 228, 'opcode': 'SWAP1'}, {'address': 229, 'opcode': 'DUP2'}, {'address': 230, 'opcode': 'PUSH8', 'argument': '0xffffffffffffffff'}, {'address': 239, 'opcode': 'AND'}, {'address': 240, 'opcode': 'DUP2'}, {'address': 241, 'opcode': 'MSTORE'}, {'address': 242, 'opcode': 'POP'}, {'address': 243, 'opcode': 'POP'}, {'address': 244, 'opcode': 'CALLVALUE'}, {'address': 245, 'opcode': 'DUP2'}, {'address': 246, 'opcode': 'MLOAD'}, {'address': 247, 'opcode': 'ADD'}, {'address': 248, 'opcode': 'DUP2'}, {'address': 249, 'opcode': 'MSTORE'}, {'address': 250, 'opcode': 'PUSH2', 'argument': '0x0109'}, {'address': 253, 'opcode': 'DUP2'}, {'address': 254, 'opcode': 'PUSH1', 'argument': '0x00'}, {'address': 256, 'opcode': 'ADD'}, {'address': 257, 'opcode': 'MLOAD'}, {'address': 258, 'opcode': 'PUSH4', 'argument': '0xffffffff'}, {'address': 263, 'opcode': 'AND'}, {'address': 264, 'opcode': 'JUMP'}]
    print("Address:", address)
    print("Bytecode:", bytecode)
    
    # vulnerabilidade ocorreu nessa instrucao {'address': 264, 'opcode': 'JUMP'}
    # no grafo, a vulnerabilidade é o nó de baixo (o no que contem o jump com address 264)
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