# Start a try block to catch errors that might occur
# when converting the user's input to an integer
try:
    # Prompt the user for input, then convert the text (a string)
    # to an integer. If the input isn't a valid whole number
    # (e.g. "cat" or "3.5"), int() raises a ValueError.
    x = int(input("What's x? "))

    # This line only runs if the conversion above succeeded.
    # The f-string inserts the value of x into the output.
    print(f"x is {x}")

# Runs only if a ValueError was raised inside the try block
except ValueError:
    # Tell the user their input couldn't be converted to an integer
    print("x is not an integer")
