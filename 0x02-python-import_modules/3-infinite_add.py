#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    tot = 0
    if n != 0:
    for i in sys.argv:
        tot += int(i)
    print("{}".format(tot))
    else:
        print("{}".format(tot))    
