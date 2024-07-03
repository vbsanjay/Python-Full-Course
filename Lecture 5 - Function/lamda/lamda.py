# Write a lambda function to add 10 to a given number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Use a lambda function to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Use a lambda function with `map()` to square all the numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Sort a list of tuples based on the second element using a lambda function
tuples = [(1, 3), (2, 2), (3, 1)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(3, 1), (2, 2), (1, 3)]

## Write a lambda function that returns a function to raise a number to a given power
power = lambda x: lambda y: y ** x
square = power(2)
cube = power(3)
print(square(5))  # Output: 25
print(cube(2))    # Output: 8

## Combine `lambda` with `reduce` to find the product of a list of numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
