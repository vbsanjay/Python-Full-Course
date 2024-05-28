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


def hello(to="world!"):
    print("hello", to)


hello("sanjay")