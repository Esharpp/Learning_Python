# Ask user for the score on their test (Assuming it is graded from 0 to 100)
"""score = int(input("Score: "))"""

# `and` is a logical operator: the whole condition is True only if both sides are True.
# Here, score must be >= 90 and also <= 100, so it must fall in the range 90-100.
"""if score >= 90 and score <= 100:
    print("Grade: A")

elif score >= 80 and score < 90:
    print("Grade: B")

elif score >= 70 and score < 80:
    print("Grade: C")

elif score >= 60 and score < 70:
    print("Grade: D")

else:
    print("Grade: F")"""

# Cleaner way to do it without using AND function
"""score = int(input("Score: "))"""

# Chained comparison: Python checks 90 <= score and score <= 100 in one expression
"""if 90 <= score <= 100:
    print("Grade: A")

elif 80 <= score < 90:
    print("Grade: B")

elif 70 <= score < 80:
    print("Grade: C")

elif 60 <= score < 70:
    print("Grade: D")

else:
    print("Grade: F")"""

# Even cleaner
score = int(input("Score: "))

# No upper bounds needed: elif only runs if the previous conditions were False,
# so by the time each check runs, the score is already below the earlier thresholds
if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")
