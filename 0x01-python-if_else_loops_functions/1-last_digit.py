#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Get the last digit of the number
digit = abs(number) % 10

# Adjust the digit for negative numbers
if number < 0:
    digit = -digit

# Print the message based on the last digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")

if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
