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

def test_custom_jumpdest():
    try:
        # Configuração básica do WorldState
        world_state = WorldState()
        
        # Configuração da conta
        active_account = Account("0x0", code=Disassembly("60606040"))  # Código de exemplo: PUSH1 0x40
        
        # Configuração do Environment
        environment = Environment(
            active_account,
            None,
            SymbolicCalldata("2"),  # Calldata simbólico
            None,
            None,
            None,
            None
        )
        
        # Configuração do MachineState
        machine_state = MachineState(gas_limit=8000000)
        
        # Criação da transação simbólica
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
        call_value2 = symbol_factory.BitVecSym("call_value2", 256)
        raw_value = Concat(
            symbol_factory.BitVecVal(0, 8),
            Extract(31, 8, 268 + call_value2),
            Extract(7, 0, call_value2) + 12
        )
        
        # Configuração da stack
        state.mstate.stack = [raw_value]
        
        # Adição de constraints
        state.world_state.constraints.add(call_value2 == 0x1234)
        
        # Execução do detector
        detector = ArbitraryJump()
        issues = detector._analyze_state(state)
        
        print(f"Vulnerabilidades encontradas: {len(issues)}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")

test_custom_jumpdest()