# Grade bands. Prompt for a score from 0 to 100 and print a letter grade: A (90+), B (80–89), C (70–79), D (60–69), F (below 60).
# Use if/elif/else. Then try reordering your branches (check the lowest band first) and explain what goes wrong.
score = int(input("What was your score /100? ").strip())

if score > 100:
    print("Not a valid score")

elif 100 >= score >= 90:
    print("Grade: A")

elif 90 > score >= 80:
    print("Grade: B")

elif 80 > score >= 70:
    print("Grade: C")

elif 70 > score >= 60:
    print("Grade: D")

elif score < 0:
    print("Not a valid score")

else:
    print("Grade: F")

# If I change the order it should not matter as long as the 1st conditional is an "if" and the ones following are "elif". 
# The "else" conditional can only be last 