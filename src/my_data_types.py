# we know about numbers
x = 44 # int
y = 47.2 # float

# we know about strings

hello = 'greet'

# we know about list and tuple
k = [x, y, True]
j = (1,) # this is a one-member tuple
print(type(j))
# all of the above are ordinal

# we have 2 non-ordinal collections
# a dictionary is a collection of key-value pairs
g = {'fn': 'Flotation', 'ln': 'Device', 'type': 'equipment'}

print(g, type(g))

# to access we use the key
print(g['fn'])

# we can iterate over the disctionary
for (k, v) in g.items():
    print(f'{k} contains {v}')

# we also have a 'set' data type
# a set is not ordinal, and may contain most simple data types
# a set can only contain unique values
data = {3, 2, 7, -2, 'a', True}
data.add(99)
data.add(2)
data.add(1)
print(data, type(data))