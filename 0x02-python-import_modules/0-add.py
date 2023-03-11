#!/usr/bin/python3
if __name__ == "__main__":
    """Imports add function from add_0 to use"""

    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
