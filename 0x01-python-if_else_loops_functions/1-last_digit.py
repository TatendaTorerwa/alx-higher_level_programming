#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
the_digit = abs(number) % 10
if number < 0:
    the_digit = -the_digit
    print("Last digit of {} is {} and is".format(number, the_digit), end="")
if the_digit > 5:
    print("is greater than 5")
elif the_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
