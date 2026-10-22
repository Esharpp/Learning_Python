def main():
    # input() always returns a string, e.g. "7:30"
    time = input("What time is it? ")

    # Convert the string to a float (7:30 -> 7.5), then check if it falls
    # inside the breakfast window. Chained comparison: 7 <= x <= 8 means
    # "x is at least 7 AND at most 8". Both ends are inclusive.
    if 7 <= convert(time) <= 8:
        print("breakfast time")

    # elif only runs if the check above was False
    elif 12 <= convert(time) <= 13:
        print("lunch time")

    elif 18 <= convert(time) <= 19:
        print("dinner time")

    # No else on purpose: if no meal matches, we print nothing at all.


def convert(time):
    # Takes a string like "7:30" and returns the total hours as a float.
    # split(":") cuts the string at the colon: "7:30" -> ["7", "30"]
    # Unpacking assigns the two pieces to two variables.
    # Both are still strings at this point.
    hours, minutes = time.split(":")
    # Turn the hours string into a whole number: "7" -> 7
    hours = int(hours)
    # Turn the minutes string into a number, then express it as a fraction
    # of an hour: "30" -> 30.0 -> 0.5
    minutes = float(minutes) / 60
    # Combine them: 7 + 0.5 = 7.5
    converted_time = hours + minutes
    # return sends the answer back to whoever called convert()
    return converted_time


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# WHAT IS `if __name__ == "__main__":` ?
#
# THE PROBLEM
# A Python file can be used in two different ways:
#   1. Run directly:  `python meal.py`
#      -> You want the program to start (ask for the time, print a meal).
#   2. Imported by another file:  `import meal`
#      -> Someone may only want to borrow a function like convert().
#      -> They do NOT want the program to start asking "What time is it?"
#         the moment they import it.
# Python needs a way to tell these two situations apart.
#
# HOW IT WORKS
# Every Python file automatically gets a built-in variable called __name__.
# Python sets it for you, and its value depends on how the file is used:
#   - Run directly      -> __name__ is the string "__main__"
#   - Imported elsewhere -> __name__ is the file's name, e.g. "meal"
#
# So this line reads in plain English as:
#   "If this file is the one being run directly, then call main()."
#
#   Situation                 | __name__ is | Does main() run?
#   --------------------------|-------------|-----------------
#   python meal.py            | "__main__"  | Yes
#   another file: import meal | "meal"      | No
#
# When the file is imported, the def blocks above are still read, so the
# other file can use meal.convert("7:30"). But main() stays quiet until
# someone calls it on purpose.
#
# WHY IT MATTERS HERE
# A checker can import this file and test convert() on its own, without the
# program hanging on an input() prompt. Without this guard, importing the
# file would immediately start the whole program.
#
# WHY IT GOES AT THE BOTTOM
# Python reads a file top to bottom. The def lines must be read before
# anything is called, so the call comes last. By the time Python reaches
# this line, both main() and convert() already exist.
#
# WHY CALL main() INSTEAD OF WRITING THE CODE DIRECTLY HERE
# Keeping the logic inside main() stops variables like `time` from leaking
# into the global space, and it is the standard Python convention.
#
# ANALOGY
# Think of the file as a restaurant kitchen. Importing is a customer reading
# the menu and ordering one dish (convert). Running directly is opening for
# full evening service (main). This line is the manager checking: "Are we
# actually open tonight, or is someone just looking at the menu?"
# ---------------------------------------------------------------------------
