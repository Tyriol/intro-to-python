# we structure code using indentation
# if incorrectly indented the code won't compile

x = True

# we indent any code block
# a code block comes after a colon
if x:
    print('This is a true statement')
    print('The code block ends when we stop indenting')
else:
    print('Not so true')

# the code block ends when there is no more indentation

# this is useful for validation (checking data is the right type)
value = input('please enter a positive integer: ')
# we need to validate the input is an integer and positive
# WARNING: input is ALWAYS a string
print(type(value))
# we can check if the input string looks like an integer
print(value.isnumeric())

if value.isnumeric(): # an integer can only be a positive whole number 
    num = int(value)
    if num > 0:
        print(f'Thank you, you entered: {num}')
else:
    print('not a positive number')

# a loop
l = [2, 4, 6, 8, 10]
for i in l:
    if i == num:
        print(f'{i} matches {num}')
    else:
        print(f'{i} does not match {num}')
