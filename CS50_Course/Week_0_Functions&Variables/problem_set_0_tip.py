# Asks the user for the meal cost and tip percentage, multiplies them,
# and prints the tip to 2 decimal places with a $ in front
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# Strips the $ from the user's input and converts it to a float (decimal value)
def dollars_to_float(d):
    return float(d.strip("$"))


# Strips the % and divides by 100 so main can multiply directly
# (15% becomes 0.15)
def percent_to_float(p):
    return float(p.strip("%")) / 100


main()
