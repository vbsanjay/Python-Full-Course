# Define a list
my_list = [1, 2, 3, 4, 5]

# 1. Using a for loop to iterate over the list
print("Using a for loop:")
for item in my_list:
    print(item)  # Prints each item in the list

# 2. Using a for loop with range to iterate over the list by index
print("\nUsing a for loop with range:")
for i in range(len(my_list)):
    print(my_list[i])  # Prints each item in the list

# 3. Using a while loop to iterate over the list
print("\nUsing a while loop:")
i = 0
while i < len(my_list):
    print(my_list[i])  # Prints each item in the list
    i += 1  # Increment the index

# 4. Using list comprehension to iterate over the list and print each item
print("\nUsing list comprehension:")
[print(item) for item in my_list]  # Prints each item in the list

# 5. Using enumerate to iterate over the list with index and value
print("\nUsing enumerate:")
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")  # Prints index and item

# 6. Using map to iterate over the list and print each item
print("\nUsing map function:")
def print_item(item):
    print(item)
list(map(print_item, my_list))  # Prints each item in the list

# 7. Using itertools.cycle to iterate over the list infinitely
print("\nUsing itertools.cycle:")
import itertools
for item in itertools.cycle(my_list):
    print(item)  # Prints each item in the list
    break  # Remove this break to iterate infinitely

# 8. Using iter and next to iterate over the list
print("\nUsing iter and next:")
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)  # Prints each item in the list
    except StopIteration:
        break  # Exit the loop when iterator is exhausted


#9. For loop with else statement
print("\nFor loop with else statement:")
for i in range(7):
    print(i, end = " ")
    if i == 8:
        break
else:
    print("All numbers were printed")

# 10. While loop with else Statement
print("\nWhile loop with else statement:")
temp = 1
while(temp < 10):
    print(temp)
    if(temp % 3 == 0):
        pass
    temp += 1
else:
    print("No break statement executed")