# Simplify the logic.
# Rewrite this without any if/else, using a single return of a boolean expression:
# Then write a version that also lets anyone aged 16 or over ride regardless of height.
"""def can_ride(height, age):
if height >= 120:
    if age >= 8:
        return True
    else:
        return False
else:
    return False"""


# Solution
def main():
    height = int(input("Height in cm: "))
    age = int(input("Age: "))

    if can_ride(height, age):
        print("Can ride")
    else:
        print("Cannot ride")


def can_ride(height, age):
    return (height >= 120 and age >= 8) or age >= 16


main()
