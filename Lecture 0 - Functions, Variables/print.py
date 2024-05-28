print("some default string functions")
name = input("Whats your name? ")
print("striping white space and capitalizing before printing the name")
# name = name.strip()
# name = name.title()
# method chaining
name = name.strip().title()
# name = input("Whats your name? ").strip().title()

print("hello", name)  # print function
print()

# f-String
print(f"hello {name} is printed using f string")
print()

# escaping character
# an escape character is a backslash (\) followed by a character that has a special meaning.
print("'Harry Potter' is my favourite movie")
print('It\'s a beautiful day')
print("She said, \"Hello\"")
print()

# split user's name
print("using split in string")
name_array = name.split(" ")
first_name, second_name = name.split(" ")
print("your first name is", first_name)
print("your second name is", name_array[1])



