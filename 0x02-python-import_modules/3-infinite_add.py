#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    tot = 0
    if n != 0:
    for i in sys.argv:
        if i != sys.argv[0]:
            tot += int(i)
    else:
    print(tot)    
