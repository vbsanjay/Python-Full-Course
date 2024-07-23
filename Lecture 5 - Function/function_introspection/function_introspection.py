def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# dir() function lists all the attributes and methods of the 'add' function
print(dir(add))

# __name__ attribute returns the name of the function
print(add.__name__)  # Output: 'add'

# __class__ attribute returns the class type of the function object
print(add.__class__)  # Output: <class 'function'>

# __doc__ attribute returns the docstring of the function, if defined
print(add.__doc__)  # Output: The docstring of the function

import inspect

# Get the name of the function
print(inspect.getmembers(add, predicate=inspect.isfunction))

# Get the source code of the function
print(inspect.getsource(add))

# Get the docstring of the function
print(inspect.getdoc(add))

# Get the arguments of the function
print(inspect.signature(add))