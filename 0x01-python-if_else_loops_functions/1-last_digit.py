#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the message based on the last digit
message = f"Last digit of {number} is {last_digit} and is"

if last_digit > 5:
    print(message, "greater than 5")
elif last_digit == 0:
    print(message, "0")
else:
    print(message, f"less than 6 and not 0")
