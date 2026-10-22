def main():
    # input() always returns a string, even if the user types numbers
    equation = input("What is your equation? ")

    # Split "x y z" on spaces into three separate strings.
    # e.g. "1 + 1" -> x = "1", y = "+", z = "1"
    x, y, z = equation.split(" ")

    # Convert the operands to floats BEFORE doing any maths.
    # Otherwise "1" + "1" would join the text into "11" instead of adding.
    x = float(x)
    z = float(z)

    # Pick the operation based on the operator (y).
    # The result is formatted with :.1f at the print, so the functions
    # themselves only calculate and return real numbers.
    # Note: the format spec goes INSIDE the braces, with no spaces.
    if y == "+":
        print(f"{add(x, z):.1f}")
    elif y == "-":
        print(f"{subtract(x, z):.1f}")
    elif y == "*":
        print(f"{multiply(x, z):.1f}")
    # No zero check needed: the problem guarantees z won't be 0 for division
    elif y == "/":
        print(f"{divide(x, z):.1f}")


# Each helper does one job: calculate and return a number.
# Display/formatting is handled in main(), not here.
def add(x, z):
    return x + z


def subtract(x, z):
    return x - z


def multiply(x, z):
    return x * z


def divide(x, z):
    return x / z


main()
