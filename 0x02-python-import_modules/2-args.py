#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        if n == 1:
            print("{} {}:".format(n, argument))
        if n > 1:
             print("{} {}:".format(n, arguments))
        for i in sys.argv:
            n = 1
            print("{}: {}".format(n, i))
            n += 1
