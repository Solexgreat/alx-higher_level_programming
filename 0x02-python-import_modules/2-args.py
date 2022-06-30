#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        n = len(sys.argv)
        for i in range(n):
            print("{} {}:".format(i + 1, "argument" if n == 2 else "arguments"))
            print("{}: {}".format(i + 1, sys.argv[i]))
