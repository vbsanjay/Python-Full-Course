thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # str

# Tuple slicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
thistuple = thistuple[2:5]
print(thistuple)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(x, y, z) = red
print(x)
print(y)
print(z)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Using _ for unused variables
my_tuple = (1, 2, 3)
a, _, c = my_tuple
print(a)  # Output: 1
print(c)  # Output: 3

# Convert a tuple to a list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]


# Convert a list to a tuple
my_list = [1, 2, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
