# Chained comparisons.
# Python allows 18 <= age < 65.
# Use this to write is_working_age(age).
# Then explain why 0 < x < 10 is not the same as 0 < x and 10 as a test.
def main():
    age = int(input("How old are you? "))
    if is_working_age(age):
        print("You are of working age")
    else:
        print("Your are not of working age")


def is_working_age(age):
    return 18 <= age < 65


# The below wouldn't work because "and 65" is not a comparison.
# Python only checks whether 65 is truthy (it always is), so the upper limit is never tested.
# It would accept any age over 18, including 200.
"""def is_working_age(age):
    return 18 < age and 65"""


main()
