# Define a string
my_string = "hello"

# 1. Using a for loop to iterate over the string
print("Using a for loop:")
for char in my_string:
    print(char)  # Prints each character in the string

# 2. Using a for loop with range to iterate over the string by index
print("\nUsing a for loop with range:")
for i in range(len(my_string)):
    print(my_string[i])  # Prints each character in the string

# 3. Using a while loop to iterate over the string
print("\nUsing a while loop:")
i = 0
while i < len(my_string):
    print(my_string[i])  # Prints each character in the string
    i += 1  # Increment the index

# 4. Using list comprehension to iterate over the string and print each character
print("\nUsing list comprehension:")
[print(char) for char in my_string]  # Prints each character in the string

# 5. Using enumerate to iterate over the string with index and character
print("\nUsing enumerate:")
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")  # Prints index and character

# 6. Using map to iterate over the string and print each character
print("\nUsing map function:")
def print_char(char):
    print(char)
list(map(print_char, my_string))  # Prints each character in the string

# 7. Using iter and next to iterate over the string
print("\nUsing iter and next:")
iterator = iter(my_string)
while True:
    try:
        char = next(iterator)
        print(char)  # Prints each character in the string
    except StopIteration:
        break  # Exit the loop when iterator is exhausted

# 8. Using itertools.cycle to iterate over the string infinitely
print("\nUsing itertools.cycle:")
import itertools
for char in itertools.cycle(my_string):
    print(char)  # Prints each character in the string
    break  # Remove this break to iterate infinitely
