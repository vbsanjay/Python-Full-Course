# Function

## What is a function in Python?
A function in Python is a block of reusable code that performs a specific task. It can take inputs, process them, and return a result.

## How does Python handle function declaration and execution order within a script?
- Python executes code sequentially, so when a function is called (like form() in your example), Python looks for a function definition with that name either before or at the point of execution.
- Python executes the script line by line. When form() is called at the end of the script, Python has already seen the definition of name_setter() above it and can execute name_setter() without any issues.
- For department_setter(), even though its definition appears after form() where it's called, Python only needs to have seen its definition by the time form() tries to execute department_setter().
- This behavior is not exactly like JavaScript's hoisting, where functions and variables are partially hoisted to the top of their scope. In Python, functions are not hoisted to the top of the scope; rather, their definitions must simply precede their execution during the sequential execution of the script.

    ```python
    def name_setter():
        # Function definition

    def form():
        name_setter()  # Function call - name_setter() is defined above
        department_setter()  # Function call - department_setter() is defined below

    def department_setter():
        # Function definition

    form()  # Calling form() function
    ```

## What is the difference between positional and keyword arguments?
- **Positional arguments**: Arguments that are passed to a function in a specific order.
- **Keyword arguments**: Arguments that are passed to a function by explicitly specifying the parameter name and value.
```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Whiskers", "cat")    # Positional
describe_pet(animal_type="hamster", pet_name="Hammy")  # Keyword
```

## How do you define a function that accepts an arbitrary number of positional arguments?
- If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
```

## Can functions be nested in Python?
Yes, you can define functions inside other functions. These are called nested functions.
```python
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")
```

## Arbitrary Keyword Arguments, **kwargs
- If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```