# Ask for the file name, then clean it up:
# .lower() makes the check case-insensitive (cat.GIF -> cat.gif)
# .strip() removes any spaces at the start or end
file = input("File Name: ").lower().strip()

# endswith() returns True if the text ends with the given suffix
if file.endswith(".gif"):
    print("image/gif")
# Two suffixes map to the same media type, so we check both at once.
# endswith() accepts a tuple: True if the file ends with ANY item in it
elif file.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
# Anything else (unknown suffix or no suffix) gets the default type
else:
    print("application/octet-stream")
