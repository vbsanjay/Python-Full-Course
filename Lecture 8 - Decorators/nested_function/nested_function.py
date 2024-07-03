# nested function in Python
def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()
outer_function()

# nested functions access variables from the outer function
def hello(input):
    def say_hello(message):
        print("hello", message)
    say_hello(input)

hello("sanjay") # output: hello sanjay

# modify a variable from the outer function inside a nested function
def counter():
    count = 1
    def increment_counter():
        nonlocal count
        count +=1 
        print(count)
    
    increment_counter()
    increment_counter()

counter()

# closure in Python
# example 1
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function("Hello, World!")
my_func() # output: Hello, World!

# example 2
def counter(number):
    count = number
    def increment_counter():
        nonlocal count
        count +=1 
        return count
    return increment_counter

my_closure = counter(10)
print(my_closure()) # output: 11
print(my_closure()) # output: 12
