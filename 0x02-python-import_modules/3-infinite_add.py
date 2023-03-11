#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argSum = 0
    for a in argv[1:]:
        argSum += int(a)
    print("{:d}".format(argSum))
