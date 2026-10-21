name = input("What's your name? ")

# If the names give is Harry, Ron or Hermione then print "Gryffindor"
"""if name == "Harry" or name == "Ron" or name == "Hermione":
    print("Gryffindor")

# If the name is Draco, print slytherin
elif name == "Draco":
    print("Slytherin")

# If the name does not match the names mentionned above, print "Who"
else:
    print("Who?")"""

# `match` takes a value (here, `name`) and compares it against each `case`
# pattern from top to bottom. The first pattern that matches runs its block,
# and the rest are skipped. It works like an if/elif chain, but reads more
# cleanly when checking one value against many options.
match name:
    # `|` means "or", so this case matches if name is any one of these three
    # values. It lets us share one block instead of repeating the same
    # print for each name.
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    # If none of the cases match (e.g. name is "Luna"), nothing runs,
    # since there is no default `case _:` here.
    case "Draco":
        print("Slytherin")
    # `_` is a wildcard that matches anything, so this case acts as the
    # default: it runs only if none of the cases above matched.
    case _:
        print("Who ?")
