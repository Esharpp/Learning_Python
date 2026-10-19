def main():
    noun = input("Please provide a noun ->").strip().capitalize()
    verb = input("Please provide a verb ->").strip()
    adjective = input("Please provide an adjective ->").strip()
    sentence = madlibs(noun, verb, adjective)
    print(sentence)


def madlibs(noun, verb, adjective):
    return f"{noun} likes to {verb} with a {adjective} ball"


main()


# print(f"{noun} likes to {verb} with a {adjective} ball")
