# Time-of-day greeting.
# Prompt for a time in 24-hour format like 14:30.
# Print Good morning (before 12:00), Good afternoon (12:00 to 17:59) or Good evening (18:00 onward).
# You’ll need to split the string and convert to int before comparing.
# Decide how to handle 12:00 exactly, and make sure your boundaries are right.
def main():
    time = input("What time is it? ").strip()
    if convert_time(time) < 12:
        print("Good morning!")
    elif 12 <= convert_time(time) < 18:
        print("Good afternoon!")
    elif 18 <= convert_time(time):
        print("Good evening!")


def convert_time(time):
    hours, minutes = time.split(":")
    converted_time = int(hours) + (float(minutes) / 60)
    return converted_time


main()
