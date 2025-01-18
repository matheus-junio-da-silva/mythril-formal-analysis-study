
import argparse
from sys import exit
from mythril.interfaces.cli import ANALYZE_LIST, create_analyzer_parser, get_creation_input_parser, get_output_parser, get_rpc_parser, get_runtime_input_parser, get_utilities_parser
from mythril.mythril.mythril_analyzer import MythrilAnalyzer
from mythril.mythril.mythril_disassembler import MythrilDisassembler

def main() -> None:
    try:    
        """The main CLI interface entry point."""

        rpc_parser = get_rpc_parser()
        utilities_parser = get_utilities_parser()
        runtime_input_parser = get_runtime_input_parser()
        creation_input_parser = get_creation_input_parser()
        output_parser = get_output_parser()

        parser = argparse.ArgumentParser(
            description="Security analysis of Ethereum smart contracts"
        )
        parser.add_argument("--epic", action="store_true", help=argparse.SUPPRESS)
        parser.add_argument(
            "-v", type=int, help="log level (0-5)", metavar="LOG_LEVEL", default=2
        )

        subparsers = parser.add_subparsers(dest="command", help="Commands")
        
        analyzer_parser = subparsers.add_parser(
            ANALYZE_LIST[0],
            help="Triggers the analysis of the smart contract",
            parents=[
                rpc_parser,
                utilities_parser,
                creation_input_parser,
                runtime_input_parser,
                output_parser,
            ],
            aliases=ANALYZE_LIST[1:],
            formatter_class=argparse.RawTextHelpFormatter,
        )
        create_analyzer_parser(analyzer_parser)
        # Get config values
        args = parser.parse_args()

        """parse args and execute --------------------------------------------"""
        #instancia de MythrilDisassembler
        disassembler = MythrilDisassembler(
            eth=None,
            solc_version=None,
            solc_settings_json=None,
            solc_args=None,
        )

        # address = '0x0000000000000000000000000000000000000000' _ = [<mythril.solidity.soliditycontract.SolidityContract object at 0x7fe89273f070>]
        address, _ = disassembler.load_from_solidity(
            args.solidity_files
        )  # list of files

        """execute command --------------------------------------------"""

        strategy = getattr(args, "strategy", "dfs")
        analyzer = MythrilAnalyzer(
            strategy=strategy, disassembler=disassembler, address=address, cmd_args=args
        )

    
        report = analyzer.fire_lasers(
            modules=(
                [m.strip() for m in args.modules.strip().split(",")]
                if args.modules
                else None
            ),
            transaction_count=args.transaction_count,
        )
        
        print(report.as_text())
        if len(report.issues) > 0:
            exit(1)
        else:
            exit(0)      
    except Exception as e:
        print(f"Error during analysis: {str(e)}")




if __name__ == "__main__":
    main()
    exit()
