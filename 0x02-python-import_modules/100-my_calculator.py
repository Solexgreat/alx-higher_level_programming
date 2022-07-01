#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv) - 1
    op = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
     elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
     elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
     else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
