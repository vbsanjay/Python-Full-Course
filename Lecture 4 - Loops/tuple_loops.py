# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# 1. Using a for loop to iterate over the tuple
print("Using a for loop:")
for item in my_tuple:
    print(item)  # Prints each item in the tuple

# 2. Using a for loop with range to iterate over the tuple by index
print("\nUsing a for loop with range:")
for i in range(len(my_tuple)):
    print(my_tuple[i])  # Prints each item in the tuple

# 3. Using a while loop to iterate over the tuple
print("\nUsing a while loop:")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])  # Prints each item in the tuple
    i += 1  # Increment the index

# 4. Using list comprehension to iterate over the tuple and print each item
print("\nUsing list comprehension:")
[print(item) for item in my_tuple]  # Prints each item in the tuple

# 5. Using enumerate to iterate over the tuple with index and value
print("\nUsing enumerate:")
for index, item in enumerate(my_tuple):
    print(f"Index: {index}, Item: {item}")  # Prints index and item

# 6. Using map to iterate over the tuple and print each item
print("\nUsing map function:")
def print_item(item):
    print(item)
list(map(print_item, my_tuple))  # Prints each item in the tuple

# 7. Using itertools.cycle to iterate over the tuple infinitely
print("\nUsing itertools.cycle:")
import itertools
for item in itertools.cycle(my_tuple):
    print(item)  # Prints each item in the tuple
    break  # Remove this break to iterate infinitely

# 8. Using iter and next to iterate over the tuple
print("\nUsing iter and next:")
iterator = iter(my_tuple)
while True:
    try:
        item = next(iterator)
        print(item)  # Prints each item in the tuple
    except StopIteration:
        break  # Exit the loop when iterator is exhausted
