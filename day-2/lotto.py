import random

'''
1. Ask a user to guess a number between 1 and 50. [x]
2. We give them three chances to guess.
3. We tell the whether they are above or below the guess each time they fail to guess correctly. [x]
'''

def ask(question):
    print(question)
    return input()

def isValidGuess(x):
    try:
        x = int(x)
        return (x > 0 and x <= 50)
    except ValueError:
        return False
    

lunckyNumber = random.randint(1, 50)
chances = 3
isWinner = False

print("Welcome to the poor man's lotto game.")
while chances > 0:
    if chances == 3:
        print("You have " + str(chances) + " chances in total!")
    elif chances > 1:
        print("You have " + str(chances) + " chances left!")
    else:
        print("One chance!")
    guess = ask("Guess a number between 1 and 50?")
    
    isValid = isValidGuess(guess)
    if(isValid == False):
        print("Please enter a valid guess.")
        continue
    else:
        guess = int(guess)
        if lunckyNumber == guess:
            isWinner = True
            print("Congratulations, you have won. You lucky number is " + str(lunckyNumber))
            break
        elif lunckyNumber > guess:
            print("Your guess is lower than the lucky number.")
        else:
            print("Your guess is higher than the lucky number.")
    chances -= 1
if isWinner == False:
    print("Sorry, you ran out of chances. The lucky number was: " + str(lunckyNumber))




