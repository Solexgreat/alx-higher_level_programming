#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        n = 0
        for i in sys.argv:
            print("{} {}:".format(n, "argument" if len(sys.argv) == 2 else "arguments"))
            print("{}: {}".format(n, i))
            n += 1
