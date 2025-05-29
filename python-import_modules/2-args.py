#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
