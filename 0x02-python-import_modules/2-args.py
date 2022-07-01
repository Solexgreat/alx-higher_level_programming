#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        if n == 1:
            print("{} argument:".format(n))
        else:
             print("{} arguments:".format(n))
             n += 1
        for i in range(n):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
