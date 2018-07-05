# Adventure Word Game
# the choice you make affects you and other players in the game
import string

def storyLine1():
    global name1
    name1 = input("Enter your name to start this adventure: ")
    print("Well {} ,the cave is right there. Everything you ever wanted has been promised inside. \n"
          "Just take step, and you'll have everything you ever wanted.".format(name1))
    print("But, it's unknown what's inside. Fear took you. But you know you gotta do this.")

storyLine1()

firstStep = input("Would you step inside (yes/no): ")
# took the first letter of the name
firstLetter = name1[0]

# calculate conditions

if ('n' in firstStep) or (firstStep == 'no'):
    print("We thought you were brave, people get scrared. But... we thought you were a legend")
    print("Goodbye")
elif ('y' in firstStep) or (firstStep == 'yes'):
    print("They say that people who's name's first letter is {} are legends, we thought it wasn't true.\n"
          " You proved us wrong.".format(firstLetter))

# response to q1
answer1 = "the one you feed the most"
if ('y' in firstStep) or (firstStep == 'yes'):
    print("As you walk in, a dragon landed in front of you")
    print("The dragon is different, it breathes ices")
    print("It looked at you with those cold eyes and ask to answer something for him.")
    questions1 = input("would you answer it's question: (yes/no)")
    if ('y' in questions1) or (questions1 == 'yes'):
        print("He ask: 'Two spiritual wolves are fighting, one is dark. Only recognizes greed, lust, violence, addiction, power and jealousy.'")
        print("'The other one is light. Only recogizes love, happiness, selflessness, courage, kindness and peace. These two wolves fight inside of, but you control who wins.'")
        print("'Here's the question, which wolf wins?'")
        ans1 = input(":")
        if (ans1 == answer1):
            print("Congratulation, all your dreams and desires are yours, it's just that you've always had them all along. It's always been in you")
        else:
            print("Sorry, wrong answer.")
            print("The dragon freezes you with it's breath")
    elif ('n' in questions1) or (questions == 'no'):
        print("THEN LEAVE THIS CAVE")



                
        
              
