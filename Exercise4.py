import random
import string

ch = random.choice( string.ascii_uppercase )
print( ch )

print( "Hello, try to guesse the letter!" )
sc = input()

if ch == sc :
      print( "Congratulations! You win this time!" )
else:
      print( "Sorry, but you didn't guess. Try again!" )

if int( ch, 32 ) > int( sc, 32 ):
      print( "You are too low" )
elif int( ch, 32 ) < int( sc, 32 ):
      print( "You are to high!" )
