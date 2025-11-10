import math
from fractions import Fraction
import sympy as sp

def solve_proportion():
    print("\nSolving Proportions (a/b = c/d)")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = input("Enter d (or 'x' to solve for x): ")

        if d.lower() == 'x':
            if a == 0:
                print("Error: Division by zero")
                return
            x = (b * c) / a
            print(f"Solution: x = {x}")
        else:
            d = float(d)
            # Check if a/b equals c/d
            result = (a * d) == (b * c)
            print(f"The proportion is {'true' if result else 'false'}")
            if not result:
                print(f"Cross products: {a}*{d} = {a*d} vs {b}*{c} = {b*c}")
    except ValueError:
        print("Invalid input. Please enter numbers.")

def solve_for_x():
    print("\nSolving for x in equations (ax + b = c)")
    try:
        a = float(input("Enter coefficient of x (a): "))
        b = float(input("Enter constant term (b): "))
        c = float(input("Enter right side value (c): "))

        if a == 0:
            if b == c:
                print("Infinite solutions (identity)")
            else:
                print("No solution (contradiction)")
        else:
            x = (c - b) / a
            print(f"Solution: x = {x}")
    except ValueError:
        print("Invalid input. Please enter numbers.")

def factor_square_root():
    print("\nFactoring Square Roots (√n)")
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
            return

        max_square = 1
        remaining = n

        # Find largest perfect square factor
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % (i*i) == 0:
                max_square = i*i
                remaining = n // max_square
                break

        if max_square == 1:
            print(f"√{n} cannot be simplified further")
        else:
            print(f"√{n} = {int(math.sqrt(max_square))}√{remaining}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def decimal_conversion():
    print("\nConverting Decimals to Fractions and Percents")
    try:
        decimal = float(input("Enter a decimal number: "))

        # Convert to fraction
        fraction = Fraction(decimal).limit_denominator()
        print(f"Fraction: {fraction.numerator}/{fraction.denominator}")

        # Convert to percent
        percent = decimal * 100
        print(f"Percent: {percent}%")
    except ValueError:
        print("Invalid input. Please enter a number.")

def fraction_conversion():
    print("\nConverting Fractions to Decimals and Percents")
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))

        if denominator == 0:
            print("Error: Denominator cannot be zero")
            return

        decimal = numerator / denominator
        percent = decimal * 100

        print(f"Decimal: {decimal}")
        print(f"Percent: {percent}%")
    except ValueError:
        print("Invalid input. Please enter numbers.")

def percent_conversion():
    print("\nConverting Percents to Decimals and Fractions")
    try:
        percent = float(input("Enter a percent (without % sign): "))

        decimal = percent / 100
        fraction = Fraction(decimal).limit_denominator()

        print(f"Decimal: {decimal}")
        print(f"Fraction: {fraction.numerator}/{fraction.denominator}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("Multi-Function Calculator")
    print("=========================")

    while True:
        print("\nSelect an operation:")
        print("1. Solve proportions")
        print("2. Solve for x in equations")
        print("3. Factor square roots")
        print("4. Convert decimals to fractions and percents")
        print("5. Convert fractions to decimals and percents")
        print("6. Convert percents to decimals and fractions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            solve_proportion()
        elif choice == '2':
            solve_for_x()
        elif choice == '3':
            factor_square_root()
        elif choice == '4':
            decimal_conversion()
        elif choice == '5':
            fraction_conversion()
        elif choice == '6':
            percent_conversion()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()