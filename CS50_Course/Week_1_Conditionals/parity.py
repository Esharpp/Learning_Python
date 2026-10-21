# Prompt user to give an x and y value // int() will always return a whole number i.e. int(3.9) -> 3
"""x = int(input("What's x? "))"""

# % is the modulo operator: it returns the remainder after division.
# Example: 7 % 2 = 1 (7 = 3*2 + 1), while 8 % 2 = 0 (8 divides evenly).
# If x % 2 == 0, there is no remainder, so x is even.
"""if x % 2 == 0:
    print("Even")
if x % 2 == 0:
    print("Even")

else:
    print("Odd")"""


# Better way to do the above
def main():
    # Ask the user for a number and convert the input (a string) to an integer
    x = int(input("What's x? "))

    # Call is_even(), which returns True if x is divisible by 2, else False,
    # and print the matching label
    if is_even(x):
        print("Even")
    else:
        print("Odd")


"""def is_even(n):
    # Check whether n is evenly divisible by 2 using the modulo operator (%),
    # which returns the remainder of the division.
    # A remainder of 0 means n is even, so return True; otherwise return False.
    if n % 2 == 0:
        return True
    else:
        return False"""


"""def is_even(n):
    # Return True if n is even, otherwise False.
    # n % 2 is the remainder after dividing n by 2: 0 means even, 1 means odd.
    # A conditional expression (value_if_true if condition else value_if_false)
    # turns that check into a single-line return.
    return True if n % 2 == 0 else False"""


# `n % 2` is the remainder after dividing n by 2 (0 if even, 1 if odd).
# Comparing it with `== 0` already produces True or False, so we can
# return that result directly.
# the standard way to write it in Python.
def is_even(n):
    return n % 2 == 0


main()
