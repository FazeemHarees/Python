import random
import math
# Reading the values of lower and upper bounds to set the range to generate the random number.
lower = int(input("Enter the lower bound:")) #Lower bound
upper = int(input("Enter the upper bound:")) #Upper bound
x = random.randint(lower,upper) #Generating the random number
print("The number of chances to guess the random number will be:",round(math.log(upper-lower+1,2))) # Generating the number of times the guess can be allowed.
count = 1
while count<math.log(upper-lower+1,2):
    count+=1
    guess = int(input("Enter the guess value:"))
    if guess==x:
        print("The value is correct")
        break
    elif guess<x:
        print("The value is lower")
    else:
        print("The value is greater")
    
    if count>=math.log(upper-lower+1,2):
        print("Sorry, but the chances are over")
        print("Randomly generated value is",x)
