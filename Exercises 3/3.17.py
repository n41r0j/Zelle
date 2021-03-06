__author__ = 'Jorian'
import math

def main():
    print("This program calculates square root using Newton's method.")
    print()

    x = eval(input("Enter number to find the root of: "))
    n = eval(input("How many iterations should I use? "))

    guess = x / 2.0
    for i in range(n):
        guess = (guess + x/guess)/2.0

    print()
    print("Approximate square root:", guess)
    print("Difference from math.sqrt:", math.sqrt(x) - guess)

main()