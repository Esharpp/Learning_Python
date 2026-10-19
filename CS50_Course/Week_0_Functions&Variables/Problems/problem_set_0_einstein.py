c = 300000000  # Speed of light in m/s


# Ask the user for a number to assign to a mass (m) and then print it
def main():
    m = int(input("m: "))
    print(f"E: {energy(m)}")


# Use the previous mass input and multiply it by c^2 (speed of light squared)
def energy(m):
    return m * (c**2)


main()
