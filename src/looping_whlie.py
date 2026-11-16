# there are a few kinds of loops in Python

def game():
    '''Here we will ask the user to enter a value
    If the enter 'quit' then the program ends
    If a positive integer is entered, convert and show the value
    for all other entries, explain that a number is needed'''
    running = True
    totalValue = 0
    while running: # this is often called a 'run loop'
        userResponse = input('Please enter a value: ')
        if userResponse == 'quit':
            print(f'Thanks for playing this pointless game, your final value was {totalValue}...goodbye')
            running = False # this will stop the while loop
        elif userResponse.isnumeric():
            num = int(userResponse)
            totalValue = totalValue + num
            print(totalValue)
        else:
            print('You need to provide an integer')

game()