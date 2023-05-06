from margatsni.__version__ import __version__
from margatsni.cli.commands import MARGATSNI_COMMANDS

from minet.cli.run import run

def main():
    run("margatsni", "%s" % __version__, MARGATSNI_COMMANDS)


if __name__ == "__main__":
    main()
