#!/usr/bin/python3
def fizzbuzz():
    """Function that prints FizzBuzz in 1 to 100"""
    for fb in range(1, 101):
        if (fb % 3 == 0) and (fb % 5 == 0):
            print("FizzBuzz ", end="")
        elif (fb % 3 == 0):
            print("Fizz ", end="")
        elif (fb % 5 == 0):
            print("Buzz ", end="")
        else:
            print(f"{fb}", end=" ")
