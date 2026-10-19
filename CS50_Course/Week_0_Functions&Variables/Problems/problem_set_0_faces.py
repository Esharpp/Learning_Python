# Create main function which will ask the user to input :) or :( then run the convert function to convert the characters into an emoji
def main():
    smile = input("Are you feeling :) or :( -> ")
    result = convert(smile)
    print(result)


# Convert :) and :( in the text into emojis, then return the result
def convert(smile):
    smile = smile.replace(":)", "🙂")
    smile = smile.replace(":(", "🙁")
    return smile


main()
