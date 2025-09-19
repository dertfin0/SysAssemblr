#
# DFHub SysAssemblr
# Version 0.1a
#

import argparse
import yaml
from colorama import Style

from utils import connection_check

argument_parser = argparse.ArgumentParser(
    prog="SysAssemblr",
    description="Utility for custom system assemble"
)
argument_parser.add_argument("configuration_file", default="none")

config = {}

if __name__ == "__main__":
    args = argument_parser.parse_args()
    if args.configuration_file == "none":
        print("Configuration file not specified!")
        exit(1)
    if not connection_check.check():
        print("Network is unreachable!")
        exit(1)

    with open(args.configuration_file, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    print(f"{Style.BRIGHT}"
          f"Welcome to {config['sys-name']} installer!"
          f"{Style.RESET_ALL}")