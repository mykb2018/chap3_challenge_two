# Write a program that prints a message if a variable is less than 10,
# and different message if the varable is greater than or equal to 10.

from random import *

x = randint(1, 20)
if x < 10:
    print("Number " + str(x) + " is less than 10.")
else:
    print("Number " + str(x) + " is greater or equal to 10.")