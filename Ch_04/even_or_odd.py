import sys

while True:
    number_str = input("Please input a number (0 to quit): ")

    # Validate input
    if not number_str.isdigit():
        print("Please enter a valid number.")
        continue

    number = int(number_str)

    if number == 0:
        print("Thank you. Game over.")
        sys.exit()

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
