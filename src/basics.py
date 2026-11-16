# This is a comment

# Python has some data types
a = 1 # we assign the value 1 to the var 'a'
b = 7.3 # this is a floating point number

print(a, b)
print('Type of a is: ', type(a))

c = 'this is a string' # a string is an immutable ordinal collection of characters
# ordinal means this collection is in a numeric order: 0, 1, 2, 3, 4 ...
print(c)
print(c[2]) # this will be the letter i
# we may use [] to 'slice' any part of the collection
print(c[0:7]) # [start:stop-before]

# other data types
boo = True # or False - boolean
l = [4, 3, 2, 5.5, 'hello', False] # this is a mutable ordinal collection of any data type (list)
l.append('appended')
print(l)

d = (6, 5, 4) # this is a mutable ordinal collection of any data type