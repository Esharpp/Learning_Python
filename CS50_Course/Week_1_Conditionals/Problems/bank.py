def main():
    # Ask the user a question, remove leading whitespace ".lstrip()", and convert to lowercase
    greeting = input("Greeting: ").lstrip().lower()

    # Calls is_hello() which returns True if greeting starts with the word "hello"
    if is_hello(greeting):
        print("$0")
    # Calls is_h() which returns True if greeting starts with the letter "h". ONLY HAPPENS IF IT DOES NOT CONTAIN HELLO
    elif is_h(greeting):
        print("$20")
    else:
        print("$100")


# Look for "hello" at the start of greeting and return the bool
def is_hello(greeting):
    return greeting.startswith("hello")


# Look for "h" at the start of greeting and return the bool
def is_h(greeting):
    return greeting.startswith("h")


main()
