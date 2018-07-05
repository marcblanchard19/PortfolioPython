# this is guess the number game
# first, I'm going to import the random module

import random as ran
#then I'm going to set the random module to a variable

callNum = ran.randint(0, 10)

# then I ask the user for a number

userAns = input("Please, guess the number I'm thinking of: ")


int(userAns)

while callNum != userAns:
    print("Please try again")
    userAns = input("Please, input the number I'm guessing: ")
    if callNum == userAns:
        print("You guessed it right!! Congratulation")
        break



