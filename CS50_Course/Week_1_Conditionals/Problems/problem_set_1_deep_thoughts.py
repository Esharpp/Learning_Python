# Ask the user a question, remove surrounding whitespace, and convert to lowercase
answer = input("What is the answer to the Great Question of Life? ").strip().lower()

# Print "Yes" if the answer is 42 (as a number or in words), otherwise print "No"
match answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
