"""# Ask user for their name
name = input("What's your name ?")

# Remove whitespace from string
name = name.strip()

# Capitalize user's name
name = name.title()"""

"""# Do all the above in one line
name = input("What's your name ?").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user {name} // Use first or last name {first} or {last}
print(f"Hello, {name}")"""

# https://docs.python.org/3/builtins/functions.html
# https://docs.python.org/3/library/stdtypes.html#string-methods

# Define a fuction that says "Hello" TO someone.
"""def hello(to): 
    print("Hello,", to)

name = input("What's your name ?")
hello(name)"""


# Cleaner way to do the above
# Create "main" function that will ask for name and then call "hello" function
def main():
    name = input("What's your name ?")
    hello(name)


# Create "hello" function
def hello(to="world"):
    print("Hello,", to)


# Call both previously created functions
main()
