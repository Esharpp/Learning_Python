# In a file called nutrition.py,
# implement a program that prompts consumers users to input a fruit (case-insensitively)
# and then outputs the number of calories in one portion of that fruit,
# per the FDA's poster for fruits, which is also available as text.
# Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
# Ignore any input that isn't a fruit.

# A list of dictionaries: each dictionary holds one fruit's name and its calories per portion
fda = [
    {"fruit": "apple", "calories": 130},
    {"fruit": "avocado", "calories": 50},
    {"fruit": "banana", "calories": 110},
    {"fruit": "cantaloupe", "calories": 50},
    {"fruit": "grapefruit", "calories": 60},
    {"fruit": "grapes", "calories": 90},
    {"fruit": "honeydew melon", "calories": 50},
    {"fruit": "kiwifruit", "calories": 90},
    {"fruit": "lemon", "calories": 15},
    {"fruit": "lime", "calories": 20},
    {"fruit": "nectarine", "calories": 60},
    {"fruit": "orange", "calories": 80},
    {"fruit": "peach", "calories": 60},
    {"fruit": "pear", "calories": 100},
    {"fruit": "pineapple", "calories": 50},
    {"fruit": "plums", "calories": 70},
    {"fruit": "strawberries", "calories": 50},
    {"fruit": "sweet cherries", "calories": 100},
    {"fruit": "tangerine", "calories": 50},
    {"fruit": "watermelon", "calories": 80},
]

# Ask the user for a fruit and convert it to lowercase so the match is case-insensitive
user_input = input("What is your favorite fruit? ").lower()

# Go through each dictionary in the list, one at a time
for item in fda:
    # Compare the fruit name in this dictionary to what the user typed
    if item["fruit"] == user_input:
        # On a match, print just the calorie count
        print(item["calories"])
        # Stop looping, since we've found the fruit
        break

# If nothing matched, the loop finishes without printing anything,
# which satisfies "ignore any input that isn't a fruit"
