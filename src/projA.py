# here we will use random numbers, imports and range

import random # there are many libraries that come with Python <- this is how you import them
# we can also import our own modules
from using_functions import checkNumeric # this imports the entire module (aka file)
# CAREFUL: whenever we import stuff, any executable code WILL run (even if you only import the single function)

r = random.random() * 10;
s = random.randint(0, 10);
print(r, s)

print(checkNumeric(s), checkNumeric(r))

# the range object
w = range(0, 11) # (start, stop-before, step=1)
print(type(w))
for i in w:
    print(i)

# a range can handle calculations
for i in w:
    # is it even
    if i%2 == 0:
        print('even')
    # odd
    if i%2 != 0:
        print('odd')
    # or a squared number
    if type(i**0.5) == int:
        print("You're a square")