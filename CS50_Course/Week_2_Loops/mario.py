"""# Define the main function, which acts as the entry point of the program.
# Its only job is to call print_column with a height of 3
def main():
    print_column(3)
# Define a function that prints a vertical column of "#" characters.
# `height` is a parameter: how many rows (lines) the column should have
def print_column(height):
    # Repeat the indented code `height` times.
    # range(height) produces the numbers 0, 1, 2 (for height=3), but we don't need them,
    # so the loop variable is named `_`, the Python convention for "unused value"
    for _ in range(height):
        # Print a single "#". print() adds a newline by default,
        # so each "#" lands on its own line, forming a column
        print("#")"""

"""# Define the main function, the entry point of the program.
# It calls print_row with a width of 4
def main():
    print_row(4)
# Define a function that prints a horizontal row of "?" characters.
# `width` is a parameter: how many "?" characters the row should contain
def print_row(width):
    # Multiplying a string by a number repeats it, so "?" * 4 gives "????".
    # print() then outputs that whole string on a single line
    print("?" * width)"""


# Define the main function, the entry point of the program.
# It calls print_square with a size of 3
def main():
    print_square(3)


# Define a function that prints a square of "#" characters.
# `size` is a parameter: it sets both the number of rows and the number of "#" per row
def print_square(size):
    # Repeat the indented code `size` times, once for each row of the square.
    # `i` counts 0, 1, 2 (for size=3) but isn't used inside the loop,
    # so `_` would be the conventional name instead
    for i in range(size):
        # Multiplying a string by a number repeats it, so "#" * 3 gives "###".
        # print() outputs that string on its own line, forming one row
        print("#" * size)


# This condition is True only when the file is run directly (e.g. `python file.py`),
# and False when the file is imported as a module into another program.
# It makes sure main() runs only in the first case
if __name__ == "__main__":
    main()
