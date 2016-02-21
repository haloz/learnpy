import sys
import getopt


def _usage():
    print("""
Usage:
    -s jenkins server url incl. protocol    (*)
    -u username
    -p password
    -j jenkins job name                     (*)
    -t start date in format "yyyy.mm.dd"    (*)
        """)
    return


def main(argv):
    server = username = password = jobname = startdate = None

    try:
        opts, args = getopt.getopt(argv, "s:u:p:j:d:")
        if len(opts) < 3:
            _usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-s":
                server = arg
            elif opt == "-u":
                username = arg
            elif opt == "-p":
                password = arg
            elif opt == "-j":
                jobname = arg
            elif opt == "-d":
                startdate = arg
            print("opt: ", opt, ", arg: ", arg)

    except getopt.GetoptError as err:
        print(err)
        _usage()
        sys.exit(2)

    if None in (server, jobname, startdate):
        _usage()
        sys.exit(2)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
