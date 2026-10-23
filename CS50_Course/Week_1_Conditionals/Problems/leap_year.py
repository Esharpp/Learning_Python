# Leap year. A year is a leap year if it is divisible by 4, except years divisible by 100 are not leap years, unless they are also divisible by 400.
# Write is_leap(year) returning a bool. Test with 1900, 2000, 2024 and 2026.
def main():
    year = int(input("Year: ").strip())
    if is_leap(year):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


main()
