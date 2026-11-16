# here we will use random numbers, imports and range

import random # there are many libraries that come with Python <- this is how you import them
# we can also import our own modules
import using_functions # this imports the entire module (aka file)

r = random.random() * 10;
s = random.randint(0, 10);
print(r, s)

print(using_functions.checkNumeric(s))

# the range object
w = range(0, 11, 2) # (start, stop-before, step=1)
print(type(w))
for i in w:
    print(i)