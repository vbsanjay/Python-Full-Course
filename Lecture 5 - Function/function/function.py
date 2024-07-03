# function in python
def name_setter():
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    print(first_name, middle_name, sep=" ", end=" ")  # sep and end are Named parameters
    print(last_name)

# a function could be called within another function
def form():
    name_setter()
    department_setter()

def department_setter():
    dep = input("Select your department: ")
    print(dep)

form()

# default parameter values

def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, World!
greet("Alice") # Output: Hello, Alice!

# arbitrary argument
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# playaround by commenting out

# dummy = [1,2,3,4]
# dummy = "World"
dummy = {1:"one", 2:"Two"}


def test_function(dummy):
    # dummy.append(5) # output: [1,2,3,4,5]
    # dummy = "Hello".join(dummy) output: [1,2,3,4,5]
    # dummy = dummy + "world" # output: [1,2,3,4,5]
    dummy[1] = "One" #output: {1: 'One', 2: 'Two'}
    
print(dummy)
test_function(dummy)
print(dummy)