try:
    """parse args and execute"""
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

    """execute command"""

    

