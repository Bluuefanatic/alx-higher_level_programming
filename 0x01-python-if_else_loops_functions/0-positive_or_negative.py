#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is greater than 0, equal to 0, or less than 0
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
