# We may gather operations into a single function

def aFunction():
    pass # placeholder that allows for a compiling code block while waiting for the actual implementation

# here is a re-usable function to validate we have numeric values
def checkNumeric(value):
    '''check if the incoming arg val is a number
    if it is, return it, otherwise return 1 by default'''
    if type(value) in (int, float): # checking the type of something is in a tuple of allowed types (values)
        return value
    else:
        return None

def addNumbers(a, b): # here we choose to pass a couple arguments into the function
    '''A docstring (triple quotes) lets us explain the purpose of a function
    Here we will check we have numberic values and then add them
    Triple quotes lets us have multi-line comments'''
    if checkNumeric(a) and checkNumeric(b): # and === && or === ||
        return(a + b)
    else:
        return('both values must be an integer')

print(addNumbers('2', 2))
