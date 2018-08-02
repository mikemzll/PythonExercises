#The first option is using mathematical operations

from random inport random

n = random() * 900 + 100
n = int(n)
print(n)

a = n // 100
b = (n // 10) % 10
c = n % 10

# The random function generates
# random fractional number from 0 to 1
from random import random
 
# Multiplication by 900 produces an accidental
# is a number between 0 and 899. (9).
# If you add 100, you get
# from 100 to 999. (9).
n = random () * 900 + 100
 
# The fractional part is discarded, the number is displayed
n = int (n)
print (n)
 
# The first digit (the highest digit) of the number
# by dividing it to 100
a = n // 100
 
# Division by 10 completely removes the last digit of the number.
# Then finding the remainder when dividing by 10 extracts
# the last digit, which in the original number was average.
b = (n // 10)% 10
 
# The last digit (lower order) of the number is
# by finding the remainder of the division by 10.
c = n% 10
 
# The sum of digits is calculated and displayed on the screen
print (a + b + c)
