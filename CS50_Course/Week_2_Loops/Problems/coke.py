# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
# and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Cost of one Coke, in cents. This is also the starting amount due.
amount_due = 50

# Keep asking for coins for as long as the user still owes money
while amount_due > 0:
    # Tell the user how much is left to pay
    print("Amount Due:", amount_due)

    # input() returns a string, so convert it to an int
    cents = int(input("Insert coin: "))

    # Only 5, 10 and 25 are accepted coins.
    # Cleaner: if cents in (5, 10, 25):
    if cents == 5 or cents == 10 or cents == 25:
        # Valid coin: reduce what is still owed
        amount_due -= cents
    else:
        # Invalid coin: amount_due stays unchanged.
        print("Wrong coin")

# The loop only ends once amount_due is 0 or negative.
# A negative value means the user overpaid, so its absolute value is the change.
# Cleaner: print("Change Owed:", -amount_due)
#   (-amount_due works because amount_due can never be positive here,
#    and "Change Owed: X" matches the spec's exact output wording.)
print("Your change is", abs(amount_due), "cents")
