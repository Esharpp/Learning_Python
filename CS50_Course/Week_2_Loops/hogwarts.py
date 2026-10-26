"""# This program stores three student names in a list,
# then prints each name on its own line.
# Create a list called "students".
# A list is an ordered collection of items, written inside square brackets
# and separated by commas. This one holds three strings (pieces of text).
# Each item has a position (an "index") starting at 0:
#   students[0] is "Hermione"
#   students[1] is "Harry"
#   students[2] is "Ron"
students = ["Hermione", "Harry", "Ron"]
# A for loop can walk through a list, one item at a time.
# "student" is the loop variable. On each pass, Python sets it to the
# next item in the list: first "Hermione", then "Harry", then "Ron".
# The name "student" is my choice. Python doesn't care what it's called,
# but a singular name for one item from a plural list ("students") reads well.
for student in students:
    # Print the current item.
    # Unlike the earlier "meow" loops, the loop variable IS used here:
    # it holds a different name on each pass.
    print(student)
# After the last item ("Ron") has been printed, the list has run out,
# so the loop ends and the program finishes."""

# This program prints each student's name with a number in front of it,
# starting from 1 (a numbered list).
students = ["Hermione", "Harry", "Ron"]
# CHANGED: the loop now uses positions (indexes) instead of the names directly.
# len(students) is 3, so range(3) gives 0, 1, 2.
# "i" is now an index number, not a name. We need it because we want to print
# a number as well as the name.
for i in range(len(students)):
    # CHANGED: print() now receives two things, separated by a comma.
    #   i + 1        -> the index plus 1, so the numbering starts at 1, not 0
    #                   (indexes start at 0, but people count from 1)
    #   students[i]  -> the name stored at position i in the list
    # When print() gets several values, it puts a single space between them.
    print(i + 1, students[i])
