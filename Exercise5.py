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
      
      
#2nd option - by converting to the line

      from random import random
 
      n = random() * 900 + 100
      n = int(n)
      print(n)

      s = str(n)

      a = int(s[0])
      b = int(s[1])
      c = int(s[2])

      print(a+b+c)
      
      #with comments
      from random import random
 
      n = random () * 900 + 100
      n = int (n)
      print (n)

      # The number is converted to a string
      s = str (n)

      # The first [0] character of the string is extracted, converted to the whole.
      # Similarly the second [1] and the third [2].
      a = int (s [0])
      b = int (s [1])
      c = int (s [2])

      print (a + b + c)
