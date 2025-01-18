from pathlib import Path
from types import SimpleNamespace
from mythril.analysis.report import Issue
from mythril.mythril import MythrilAnalyzer, MythrilDisassembler

def analyze_contract():
    try:
        disassembler = MythrilDisassembler(eth=None, solc_version="v0.8.0")
        solidity_file_path = Path(__file__).parent.parent / "testdata/input_contracts/bridge.sol"
        
        if not solidity_file_path.exists():
            raise FileNotFoundError(f"Contract file not found: {solidity_file_path}")
            
        disassembler.load_from_solidity([str(solidity_file_path.absolute())])

        args = SimpleNamespace(
        execution_timeout=5,
        max_depth=30,
        solver_timeout=10000,
        no_onchain_data=True,
        loop_bound=None,
        create_timeout=None,
        disable_dependency_pruning=False,
        custom_modules_directory=None,
        pruning_factor=0,
        parallel_solving=True,
        unconstrained_storage=True,
        call_depth_limit=3,
        disable_iprof=True,
        solver_log=None,
        transaction_sequences=None,
        disable_coverage_strategy=False,
        disable_mutation_pruner=False,
        enable_summaries=False,
        enable_state_merging=False,
        )

        analyzer = MythrilAnalyzer(disassembler, cmd_args=args)
        issues = analyzer.fire_lasers(modules=[]).sorted_issues()
        
        if not issues:
            print("No issues found")
        else:
            for issue in issues:
                print(issue)
                
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    analyze_contract()