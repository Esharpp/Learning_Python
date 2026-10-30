# In some languages, it’s common to use camel case (otherwise known as “mixed case”)
# for variables’ names when those names comprise multiple words,
# whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase.
# For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName,
# and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.
# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase.
# For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.
# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

# Ask the user for a variable name written in camel case (e.g. preferredFirstName)
camelCase = input("What is your name? ")
# Start with an empty string; we'll build the snake case version in here
snake = ""
# Go through the input one character at a time, from left to right
for letter in camelCase:
    # An uppercase letter means a new word is starting (the "F" in preferredFirstName)
    if letter.isupper():
        # So add an underscore before it to separate the words // snake += letter is exactly the same as snake = snake + letter
        snake += "_"
    # Add the current letter itself to the result (uppercase or not)
    snake += letter

# At this point snake is "preferred_First_Name", so make everything lowercase
print(snake.lower())
