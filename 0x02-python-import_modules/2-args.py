#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 0:
    n = len(sys.argv) - 1
    print("{} arguments.".format(n))
else:
    n = len(sys.argv)
    for i in range(n):
    print("{} {}:".format(i + 1, "argument" if n == 1 else "arguments"))
    print("{}: {}".format(i + 1, sys.argv[i]))
