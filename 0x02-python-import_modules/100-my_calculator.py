#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if argv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    operation = [add, sub, mul, div]
    for i, op in enumerate(operator):
        if argv[2] == op:
            print("{} {} {} = {}".format(a, op, b, operation[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
