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

conv
