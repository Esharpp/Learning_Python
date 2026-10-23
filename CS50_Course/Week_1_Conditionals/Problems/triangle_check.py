# Triangle check.
# 1. Ask the user for three side lengths.
# 2. Check the triangle is valid:
#      - every side is positive
#      - any two sides added together are greater than the third side
# 3. If valid, print "valid" and classify it as equilateral, isosceles or scalene.
def main():
    # Read the three sides. int() converts the typed text into a whole number.
    a = int(input("Side A: "))
    b = int(input("Side B: "))
    c = int(input("Side C: "))

    # Validity check, all of these must be True (hence the "and"s):
    #   - a, b and c are each greater than 0 (each side needs its own comparison;
    #     writing "a and b and c > 0" would not check all three)
    #   - the triangle inequality: every pair of sides adds up to more than the
    #     remaining side. There are three pairs, so three comparisons.
    if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
        print("valid")
        # Classify the triangle. Order matters here:
        # equilateral (3 equal sides) is checked first, because an equilateral
        # triangle would also pass the isosceles test (at least 2 equal sides).
        if equilateral(a, b, c):
            print("The triangle is equilateral")
        elif isosceles(a, b, c):
            print("The triangle is isosceles")
        else:
            # A valid triangle that is neither equilateral nor isosceles
            # must have all three sides different, so it is scalene.
            print("The triangle is scalene")
    else:
        # Reached if any side is zero or negative, or the inequality fails
        # (e.g. 1, 1, 10 can't form a triangle).
        print("invalid")


def equilateral(a, b, c):
    # True only when all three sides are equal.
    return a == b == c


def isosceles(a, b, c):
    # True when at least two sides are equal (any one of the three pairs).
    return a == b or a == c or b == c


def scalene(a, b, c):
    # True when all three sides are different.
    # Not called in main() any more (the final else covers it), but kept
    # here in case I want to use it later.
    return a != b and a != c and b != c


main()


# Test cases to remember a/b/c
# 3/4/5 -> valid, scalene
# 2/2/3 -> valid,isosceles
# 5/5/5 -> valid,equilateral
# 1/1/10 -> invalid
# -1/5/5 -> invalid
