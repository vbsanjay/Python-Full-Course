# Define a set
my_set = {1, 2, 3, 4, 5}

# 1. Using a for loop to iterate over the set
print("Using a for loop:")
for item in my_set:
    print(item)  # Prints each item in the set

# 2. Using a while loop to iterate over the set
print("\nUsing a while loop:")
my_set_list = list(my_set)  # Convert set to list
i = 0
while i < len(my_set_list):
    print(my_set_list[i])  # Prints each item in the set
    i += 1  # Increment the index

# 3. Using list comprehension to iterate over the set and print each item
print("\nUsing list comprehension:")
[print(item) for item in my_set]  # Prints each item in the set

# 4. Using enumerate to iterate over the set with index and value
print("\nUsing enumerate:")
for index, item in enumerate(my_set):
    print(f"Index: {index}, Item: {item}")  # Prints index and item

# 5. Using map to iterate over the set and print each item
print("\nUsing map function:")
def print_item(item):
    print(item)
list(map(print_item, my_set))  # Prints each item in the set

# 6. Using iter and next to iterate over the set
print("\nUsing iter and next:")
iterator = iter(my_set)
while True:
    try:
        item = next(iterator)
        print(item)  # Prints each item in the set
    except StopIteration:
        break  # Exit the loop when iterator is exhausted

# 7. Using itertools.cycle to iterate over the set infinitely
print("\nUsing itertools.cycle:")
import itertools
for item in itertools.cycle(my_set):
    print(item)  # Prints each item in the set
    break  # Remove this break to iterate infinitely
