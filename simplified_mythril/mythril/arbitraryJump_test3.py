print("Debug: Starting import statements.")
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

print("Debug: Finished imports.")

def test_custom_jumpdest():
    print("Debug: test_custom_jumpdest() called.")

    print("Debug: Starting execution time for time_handler with 30 seconds.")
    time_handler.start_execution(30)  # 30 seconds
    
    print("Debug: Creating WorldState.")
    world_state = WorldState()
    print(f"Debug: world_state => {world_state}")

    print("Debug: Creating Account with code 60606040.")
    # Use a fully qualified address, and set the account in the world_state so that balances are tracked.
    active_account = Account("0x0000000000000000000000000000000000000000", code=Disassembly("60606040"))
    world_state.accounts[active_account.address] = active_account
    # Set a balance for the account
    active_account._balances[active_account.address] = symbol_factory.BitVecVal(1000, 256)
    print(f"Debug: active_account => {active_account}")

    print("Debug: Creating Environment.")
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
    print(f"Debug: environment => {environment}")

    print("Debug: Creating MachineState with gas_limit=8000000.")
    machine_state = MachineState(gas_limit=8000000)
    print(f"Debug: machine_state => {machine_state}")

    print("Debug: Creating MessageCallTransaction.")
    transaction = MessageCallTransaction(
        world_state=world_state,
        gas_limit=8000000,
        caller=ACTORS.attacker,
        callee_account=active_account,
        call_value=symbol_factory.BitVecSym("call_value", 256)
    )
    print(f"Debug: transaction => {transaction}")

    print("Debug: Creating GlobalState.")
    state = GlobalState(
        world_state=world_state,
        environment=environment,
        machine_state=machine_state,
        node=None
    )
    print(f"Debug: state => {state}")

    print("Debug: Appending transaction to world_state.transaction_sequence.")
    state.world_state.transaction_sequence = [transaction]
    print(f"Debug: transaction_sequence => {state.world_state.transaction_sequence}")
    
    print("Debug: Creating call_value2 BitVecSym.")
    call_value2 = symbol_factory.BitVecSym("call_value2", 256)
    print(f"Debug: call_value2 => {call_value2}")
    
    print("Debug: Building raw_value with Concat & Extract operations.")
    raw_value = Concat(
        symbol_factory.BitVecVal(0, 8),
        Extract(31, 8, symbol_factory.BitVecVal(268, 256) + call_value2),
        Extract(7, 0, call_value2) + symbol_factory.BitVecVal(12, 8)
    )
    print(f"Debug: raw_value => {raw_value}")

    print("Debug: Assigning raw_value to state.mstate.stack.")
    state.mstate.stack = [raw_value]
    print(f"Debug: state.mstate.stack => {state.mstate.stack}")

    print("Debug: Appending constraint call_value2 == symbol_factory.BitVecVal(0x1234, 256).")
    state.world_state.constraints.append(call_value2 == symbol_factory.BitVecVal(0x1234, 256))
    print(f"Debug: constraints => {state.world_state.constraints}")

    print("Debug: Instantiating ArbitraryJump detector.")
    detector = ArbitraryJump()
    print(f"Debug: detector => {detector}")

    print("Debug: Analyzing state with detector._analyze_state(state).")
    issues = detector._analyze_state(state)
    print(f"Debug: issues => {issues}")
    
    print(f"Vulnerabilidades encontradas: {len(issues)}")


print("Debug: Calling test_custom_jumpdest().")
test_custom_jumpdest()