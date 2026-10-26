"""# This program prints "meow" 3 times using a while loop.
# Create a variable called "i" and set it to 3.
# This acts as a counter: it tracks how many times we still need to print.
i = 3
# A while loop keeps repeating its indented block for as long as the
# condition is True.
# "i != 0" means "i is not equal to 0".
# So: keep looping until i reaches 0.
while i != 0:
    # Print the word "meow" to the screen.
    print("meow")

    # Subtract 1 from i, then store the result back in i.
    # This moves the counter closer to 0 each time round.
    # (You could also write this shorter as: i -= 1)
    i = i - 1

# When i becomes 0, the condition "i != 0" is False,
# so the loop stops and the program ends."""

"""# This program prints "meow" 3 times using a for loop.
# A for loop runs its indented block once for each item in a sequence.
# Here the sequence is the list [0, 1, 2], which has 3 items,
# so the loop will run exactly 3 times.
# "i" is the loop variable. On each pass, Python automatically sets it
# to the next item in the list: first 0, then 1, then 2.
# (You don't need to create it or change it yourself, unlike the while loop.)
for i in [0, 1, 2]:
    # Print the word "meow" to the screen.
    # Note: this code never actually uses the value of i. The list is only
    # there to control how many times the loop repeats.
    print("meow")
# After the last item (2) has been processed, the list has run out,
# so the loop ends and the program finishes."""

"""# This program prints "meow" 3 times using a for loop with range().
# range(3) produces the sequence 0, 1, 2 (three numbers, starting at 0
# and stopping BEFORE 3). It's a shortcut for writing the list [0, 1, 2].
# The for loop runs its indented block once per number in that sequence,
# so this loop runs exactly 3 times.
# "i" is the loop variable. Python sets it to 0 on the first pass,
# 1 on the second, and 2 on the third.
for i in range(3):
    # Print the word "meow" to the screen.
    # Note: i is never used inside the loop. It only exists to count
    # the passes. (By convention, you can write "_" instead of "i"
    # to show that you don't need the value.)
    print("meow")

# Once range(3) has run out of numbers, the loop ends and the program finishes."""

"""# This program prints "meow" 3 times, each on its own line,
# using string repetition instead of a loop.
# Step 1: "meow\n" is a string containing the word meow followed by \n.
#         \n is a special "newline" character: it moves the cursor
#         to the start of the next line (like pressing Enter).
#
# Step 2: Multiplying a string by a number repeats it that many times.
#         "meow\n" * 3 becomes "meow\nmeow\nmeow\n" (one single string).
#
# Step 3: print() sends that whole string to the screen in one go.
#
# end="" tells print() NOT to add its usual extra newline at the end.
# Normally print() adds one automatically. Here the string already ends
# with \n, so without end="" we would get a blank line after the last meow.
print("meow\n" * 3, end="")"""

"""# This program asks the user for a positive whole number (n),
# keeps asking until they give one, then prints "meow" n times.
# --- Part 1: keep asking until the input is valid ---
# "while True" creates a loop that never ends on its own,
# because the condition True is always True.
# We stop it manually with "break" once we have a valid answer.
while True:
    # input() shows the prompt "What's n? " and waits for the user to type.
    # It always returns what they typed as a string (text), e.g. "5".
    # int() converts that string into a whole number, e.g. 5.
    # The result is stored in the variable n.
    # (If the user types something that isn't a whole number, like "cat",
    # int() raises a ValueError and the program crashes. See notes below.)
    n = int(input("What's n? "))

    # Check whether the number is positive (greater than 0).
    if n > 0:
        # Valid input: "break" immediately exits the while loop
        # and the program moves on to Part 2.
        break

    # If n was 0 or negative, the "if" block is skipped,
    # the end of the loop body is reached, and Python goes back
    # to the top of the "while True" loop to ask again.
# --- Part 2: print "meow" n times ---
# range(n) produces the numbers 0 up to n - 1, which is n numbers in total,
# so this loop runs exactly n times.
# "_" is the loop variable. By convention it means "I don't need this value".
# We only care about repeating, not about the count itself.
for _ in range(n):
    # Print the word "meow" followed by a newline.
    print("meow")"""


# This program asks the user for a positive whole number (n),
# keeps asking until they give one, then prints "meow" n times.
# It is split into three functions, each with one job.
# --- Function definitions ---
# "def" creates a function: a named, reusable block of code.
# Defining a function does NOT run it. Python just remembers it.
# The code inside only runs when the function is called (see the last line).
def main():
    # main() is the "controller" of the program. It runs the steps in order.

    # Call get_number(). It asks the user for input and sends back a valid
    # positive number, which we store in the variable "number".
    number = get_number()

    # Call meow(), handing it the number we just got.
    # Inside meow(), that value will be called "n".
    meow(number)


def get_number():
    # Job: keep asking until the user types a positive whole number,
    # then hand that number back to whoever called this function.
    # "while True" loops forever, until we leave it with "return" or "break".
    while True:
        # input() shows the prompt and waits for the user to type.
        # It returns text (a string), so int() converts it to a whole number.
        # (Typing something like "cat" would crash with a ValueError.)
        n = int(input("What's n? "))
        # Only accept positive numbers.
        if n > 0:
            # "return" does two things at once:
            #   1. Sends the value of n back to the caller (to main()).
            #   2. Immediately ends this function, which also exits the loop.
            # That's why we don't need "break" here, as we did before.
            return n
        # If n was 0 or negative, we reach the end of the loop body
        # and go back to the top to ask again.


def meow(n):
    # Job: print "meow" n times.
    # "n" is a parameter: a variable that receives the value passed in
    # when the function is called. Here, it gets the value of "number" from main().
    # range(n) gives n numbers, so the loop runs n times.
    # "_" means we don't need the loop variable's value.
    for _ in range(n):
        print("meow")
    # meow() has no "return", so it gives nothing back. It only prints.


# --- Start the program ---
# This is the line that actually runs everything.
# All the "def" blocks above only define functions; this call starts main(),
# which then calls get_number() and meow().
main()
