from random import randint

def generateRandomInt():
    '''generate the random number the user has to guess'''
    return randint(0,100)

def getUserInput():
    return input('Take a guess: ')

def handleGuess(userGuess, randomNumber):
    # validate guess is an integer
    if userGuess.isnumeric():
        num = int(userGuess)
        if num == randomNumber:
            return('win')
        elif num > randomNumber:
            return('high')
        elif num < randomNumber:
            return('low')
    else:
        return None

def higherOrLowerGame():
    # print game intro
    print('Welcome to the Higher or Lower game! Guess an integer between 0 and 100.')
    print('Enter -1 to quit the game or -2 to get a hint.')
    # generate number
    numToGuess = generateRandomInt()
    numOfGuesses = 0
    # ask user to guess the number
    while True:
        guess = getUserInput()
        if guess == '-1':
            print(f'You quit the game. The number was {numToGuess}')
            break
        elif guess == '-2':
            if numToGuess % 2 == 0:
                print('Hint: The number is even')
            else:
                print('Hint: The number is odd')
        else:
        # handle the guess
            numOfGuesses += 1
            guessResult = handleGuess(guess, numToGuess)
            if guessResult == None:
                print('We need a number')
            elif guessResult == 'high':
                print('Too high, try again')
            elif guessResult == 'low':
                print('Too low, try again')
            elif guessResult == 'win':
                print('Congratulations! You guessed it!')
                print(f'It took you {numOfGuesses} guesses.')
                break

higherOrLowerGame()