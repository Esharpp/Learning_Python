# Prompt user to give an x and y value // int() will always return a whole number i.e. int(3.9) -> 3
"""x = int(input("What's x ? "))
y = int(input("What's y ? "))"""

# Compare both numbers with each other and print the answer (less, greater, equal)
"""if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")"""


# Improved version of the above
"""x = int(input("What's x ? "))
y = int(input("What's y? "))"""

# elif runs only if the previous if/elif conditions were False and its own condition is True
"""if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal to y")"""

# Even better way to do it
"""x = int(input("What's x ? "))
y = int(input("What's y? "))"""

# else runs only if none of the previous if/elif conditions were True
"""if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")"""

# Prompt user to give an x and y value // int() will always return a whole number i.e. int(3.9) -> 3
x = int(input("What's x ? "))
y = int(input("What's y? "))

# Check if the numbers are equal using the OR and ELSE function
# Can be done by doing -> if x != y:
if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")
