#
# DFHub SysAssemblr
# Version 0.1a
#

import argparse

from utils import connection_check

argument_parser = argparse.ArgumentParser(
    prog="SysAssemblr",
    description="Utility for custom system assemble"
)
argument_parser.add_argument("configuration_file", default="none")

if __name__ == "__main__":
    args = argument_parser.parse_args()
    if args.configuration_file == "none":
        print("Configuration file not specified!")
        exit(1)
    if not connection_check.check():
        print("Network is unreachable!")
        exit(1)
