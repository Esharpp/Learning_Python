# When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr.
# In a file called twttr.py,
# implement a program that prompts the user for a str of text and then outputs that same text
# but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


# Ask the user for some text
text = input("What's your name? ")

# Every character we want to remove.
# Both cases are listed so we never have to change the user's input.
# (A string works like a tuple here: "in" checks each character.)
vowels = "aeiouAEIOU"

# Start with an empty string; we'll build the result one character at a time
twttr = ""

# Go through the input one character at a time
for char in text:
    # Keep the character only if it is NOT a vowel
    if char not in vowels:
        # += adds the character to the end of our result string
        twttr += char

# Print once, after the loop is done (not inside it, or it prints on every pass)
print(twttr)
