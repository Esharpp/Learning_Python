# In Massachusetts, home to Harvard University,
# it’s possible to request a vanity license plate for your car,
# with your choice of letters and numbers instead of random ones.
#
# Among the requirements, though, are:
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate
# and then output Valid if meets all of the requirements or Invalid if it does not.
# Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
# wherein is_valid returns True if s meets all requirements and False if it does not.
# Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # RULE 1: the plate must start with at least two letters.
    # s[0:2] is a slice of the first two characters.
    # .isalpha() is True only if every character in it is a letter.
    # We use "not" because each check describes when the plate is BAD.
    if not s[0:2].isalpha():
        return False

    # RULE 2: length must be between 2 and 6 characters (inclusive).
    # Again we describe the broken case: too short OR too long.
    if len(s) < 2 or len(s) > 6:
        return False

    # RULE 3: no punctuation, spaces, or periods.
    # .isalnum() is True only if every character is a letter or digit.
    if not s.isalnum():
        return False

    # RULES 4 and 5 both involve digits, so we walk through the plate
    # one character at a time.
    #
    # seen_digit is our "memory": it starts False and flips to True the
    # moment we meet the first digit. It lets us answer two questions:
    #   - "Is this the first digit?"        -> seen_digit is still False
    #   - "Did a digit come before this?"   -> seen_digit is True
    seen_digit = False
    for char in s:
        if char.isdigit():
            # RULE 4: the first digit can't be "0".
            # This check MUST come before seen_digit = True. Once we flip
            # the flag, we can no longer tell whether this was the first digit.
            if not seen_digit and char == "0":
                return False
            seen_digit = True
        else:
            # It's a letter. RULE 5: numbers can only be at the end,
            # so a letter appearing AFTER a digit makes the plate invalid.
            if seen_digit:
                return False

    # Every check passed. This must be OUTSIDE the loop, so it only runs
    # after all characters have been checked.
    return True


if __name__ == "__main__":
    main()
