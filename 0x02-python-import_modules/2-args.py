#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        if n == 1:
            print("{} argument:".format(n))
        if n > 1:
             print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
