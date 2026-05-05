#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if number > 0:
    number_type = "is positive"
elif number < 0:
    number_type = "is negative"
else:
    number_type = "is zero"
print(f"{number} {number_type}")
