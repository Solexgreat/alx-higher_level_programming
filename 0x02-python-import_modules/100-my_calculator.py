#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
    else:
        for arg in sys.argv:
            if arg = '+':
                a = sys.argv[2]
                b = sys.argv[4]
                print("{} + {} = {}".format(a, b, add(a, b)))
                print(0)
            elif arg = '-':
                a = sys.argv[2]
                b = sys.argv[4]
                print("{} - {} = {}".format(a, b, sub(a, b)))
                print(0)
            elif arg = '*':
                a = sys.argv[2]
                b = sys.argv[4]
                print("{} * {} = {}".format(a, b, mul(a, b)))
                print(0)
            elif arg = '/':
                a = sys.argv[2]
                b = sys.argv[4]
                print("{} / {} = {}".format(a, b, div(a, b)))
                print(0)
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                print(1)
