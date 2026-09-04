import random as rd

randNum, userGuess = 0, 0
hasWon = False

randNum = rd.randint(1, 50)

while (hasWon == False):

    try:
        userGuess = int(input("Guess a number between 1 and 50: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if (userGuess < 1 or userGuess > 50):
        print("Please enter a number between 1 and 50.")
        continue
    elif (userGuess == randNum):
        print("You guessed it! The number was " + str(randNum))
        hasWon = True
    elif (userGuess < randNum):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        