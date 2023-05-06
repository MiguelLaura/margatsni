# =============================================================================
# Margatsni Argparse Helpers
# =============================================================================
#
# Miscellaneous helpers related to CLI argument parsing.
# Exaclty the same as the Minet library, but correction on the programm name
#
from argparse import (
    ArgumentParser,
)
from minet.cli.argparse import build_subparsers, custom_formatter


def build_parser(name, version, commands):

    # Building the argument parser
    parser = ArgumentParser(prog=name, formatter_class=custom_formatter)

    parser.add_argument(
        "--version", action="version", version="%s %s" % (name, version)
    )

    subparser_index = {}

    subparsers = build_subparsers(
        parser, subparser_index, {c["name"]: c for c in commands}
    )

    # Help subparser
    help_subparser = subparsers.add_parser("help")
    help_subparser.add_argument("subcommand", help="Name of the subcommand", nargs="*")

    return parser, subparser_index