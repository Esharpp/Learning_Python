# Ask user input for X and Y // int() function turns a string to a number (HAS TO BE A WHOLE NUMBER)
"""x = int(input("What's x ?"))
y = int(input("What's y ?"))

# Ask user input for X and Y // float() functions turns a string in a DECIMAL NUMBER
x = float(input("What's x ?"))
y = float(input("What's y ?"))

# Round a decimal value
z = round(x / y)

# Round to a certain number of digits -> round(number, ndigits=None)
z= round(x / y, 2)

z = x / y

# print(z) with 2 digits
print(f"{z:.2f}")"""

# f"{z:,}" adds a comma at each thousand to make it clearer to read big numbers

# https://docs.python.org/3/builtins/functions.html#round

def main():
    x = input(input("What's X ?"))
    print("x squared is", square(x))

def square(n):
    return n * n

main()