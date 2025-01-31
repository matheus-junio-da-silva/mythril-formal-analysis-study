from mythril.analysis.module.modules.arbitrary_jump import ArbitraryJump
from mythril.laser.ethereum.state.machine_state import MachineStack, MachineState
from mythril.laser.smt import BitVec, Concat, Extract, symbol_factory
from mythril.laser.ethereum.state.world_state import WorldState
from mythril.laser.ethereum.state.constraints import Constraints
from mythril.laser.ethereum.state.global_state import GlobalState
from mythril.laser.ethereum.state.world_state import WorldState
from mythril.laser.ethereum.state.account import Account

try:    
    # Inicializaçao dos componentes necessários
    world_state = WorldState()
    account = Account("0x1234")
    world_state.put_account(account)

    # valor simbólico para call_value2 (exemplo)
    call_value2 = symbol_factory.BitVecSym("call_value2", 256)

    # expressão simbólica conforme o valor original que deu origem a vulnerabilidade
    raw_value = Concat(
        symbol_factory.BitVecVal(0, 8),  # 0 (8 bits)
        Extract(31, 8, 268 + call_value2),  # Extract 24 bits (31-8) de (268 + call_value2)
        Extract(7, 0, call_value2) + 12  # Extract 8 bits (7-0) de call_value2 e soma 12
    )

    # stack personalizada
    custom_stack = MachineStack()
    custom_stack.append(raw_value)  # Adição da expressão à stack

    # Configuraçao do MachineState
    machine_state = MachineState(gas_limit=1000000)
    machine_state.stack = custom_stack

    # Atribuição da stack personalizada ao state.mstate
    #state.mstate.stack = custom_stack

    # Crie o GlobalState
    state = GlobalState(
        world_state=world_state,
        environment=None,  # Você pode precisar mockar outros componentes
        node=None,
        machine_state=machine_state
    )

    # Crie constraints simbólicas
    constraints = Constraints()
    constraints.append(call_value2 == 0x1234)  # Exemplo: call_value2 deve ser 0x1234

    # Atualize o WorldState
    state.world_state.constraints = constraints

    # Execute o detector
    detector = ArbitraryJump()
    detector._analyze_state(state)
except Exception as e:
    print(e)
    pass
