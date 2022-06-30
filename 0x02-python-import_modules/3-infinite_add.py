#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            tot += int(i)
    print(tot)    
