import sys
import argparse


def _parseArguments(argv):
    parser = argparse.ArgumentParser(
        description="QueryJenkins: a Jenkins build statistics tool.")
    parser.add_argument(
        "-s", dest="server", required=True,
        help="jenkins server url incl. protocol")
    parser.add_argument(
        "-j", dest="jobname", required=True,
        help="jenkins job name")
    parser.add_argument(
        "-d", dest="startdate", required=True,
        help="start date in format \"yyyy.mm.dd\"")
    parser.add_argument(
        "-u", dest="username", nargs="?", default=None, help="username")
    parser.add_argument(
        "-p", dest="password", nargs="?", default=None, help="password")
    return parser.parse_args()


def main(argv):
    argvdict = _parseArguments(argv)
    print(argvdict)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
