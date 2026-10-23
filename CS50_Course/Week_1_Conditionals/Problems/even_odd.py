# Even or odd. Write main() that prompts for an integer and prints even or odd. Use %. 
# Then rewrite the check as a separate function is_even(n) that returns a bool and no if statement. 
# (Hint: a comparison already evaluates to a bool.)

def main():
    x = int(input("Please provide a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(x):
   return x % 2 == 0

main()