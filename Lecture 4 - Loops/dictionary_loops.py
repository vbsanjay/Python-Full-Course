# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 1. Using a for loop to iterate over dictionary keys
print("Using a for loop (keys):")
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")  # Prints each key and value

# 2. Using a for loop with .keys() to iterate over dictionary keys
print("\nUsing .keys():")
for key in my_dict.keys():
    print(f"Key: {key}, Value: {my_dict[key]}")  # Prints each key and value

# 3. Using a for loop with .values() to iterate over dictionary values
print("\nUsing .values():")
for value in my_dict.values():
    print(f"Value: {value}")  # Prints each value in the dictionary

# 4. Using a for loop with .items() to iterate over dictionary key-value pairs
print("\nUsing .items():")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Prints each key and value

# 5. Using list comprehension to iterate over dictionary key-value pairs and print them
print("\nUsing list comprehension:")
[print(f"Key: {key}, Value: {value}") for key, value in my_dict.items()]  # Prints each key and value

# 6. Using enumerate to iterate over dictionary key-value pairs with index
print("\nUsing enumerate:")
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")  # Prints index, key, and value

# 7. Using map to iterate over dictionary items and print each key-value pair
print("\nUsing map function:")
def print_item(item):
    key, value = item
    print(f"Key: {key}, Value: {value}")
list(map(print_item, my_dict.items()))  # Prints each key and value

# 8. Using iter and next to iterate over dictionary items
print("\nUsing iter and next:")
iterator = iter(my_dict.items())
while True:
    try:
        key, value = next(iterator)
        print(f"Key: {key}, Value: {value}")  # Prints each key and value
    except StopIteration:
        break  # Exit the loop when iterator is exhausted
