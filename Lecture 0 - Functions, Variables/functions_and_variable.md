# Cli
CLI stands for Command Line Interface. It's a text-based interface used to interact with a computer program or operating system by typing commands into a terminal or console.

# Interpreted Language
## C and C++
- C and C++ are typically classified as compiled languages.
- In C and C++, code is translated into machine code, which consists of binary instructions tailored to the specific hardware architecture and operating system. 
- This process is facilitated by a compiler. 
- As a result, executables produced from C and C++ source code are platform-specific and may require recompilation to run on different platforms. 
- Once compiled, the machine code is directly executed by the CPU without additional translation steps. 
- Therefore, C and C++ programs are precompiled into executable files before being executed.
## No Compilation Step
- In Python, there's no need for a separate compilation step like in languages such as C and C++. 
- Instead, Python code is executed directly without explicit compilation. 
- This means that as each line of Python code is encountered, it's executed immediately, and the effects of that line, such as variable assignments, function calls, or changes in control flow, take effect right away. 
- This line-by-line execution approach makes Python code execution more interactive and flexible.
## Python Interpreter
- Python code is executed by the Python interpreter, which reads and interprets the code line by line. 
- The Python interpreter is a program that translates Python code into machine-readable bytecode and executes it on the fly.
## Dynamic Typing
- Python is dynamically typed, meaning you don't need to declare the data type of variables explicitly. 
- Variables are dynamically assigned data types based on the values they hold at runtime. 
- This dynamic typing feature allows for greater flexibility and ease of use but requires interpretation of variable types during execution.
## Late Binding
- Python employs late binding, also known as dynamic binding or runtime binding. 
- In languages like C++, the binding of a function to its implementation occurs at compile time. 
- However, in Python, the binding of a function to its implementation happens at runtime. 
- This means that the specific function implementation to be called is determined dynamically during program execution based on the object type.
## Portability and Platform Independence
- Since Python code is executed by the interpreter rather than directly by the underlying hardware, Python programs are highly portable and platform-independent. 
- The same Python code can run on different operating systems without modification, as long as the appropriate Python interpreter is available for each platform.

---

# Data types
## What are the basic data types in Python?
- The basic data types in Python are:
    - Integers: int 
    - Floating-point numbers: float 
    - Complex numbers: complex 
    - Strings: str 
    - Booleans: bool 
    - NoneType: None
  
## How do you convert between data types in Python?
- You can use **type casting functions** to convert between data types. Examples include:
  - int(x): Converts x to an integer. 
  - float(x): Converts x to a float. 
  - str(x): Converts x to a string. 
  - bool(x): Converts x to a boolean.

## What is the difference between a list and a tuple?
- List: A mutable, ordered collection of items. Defined with square brackets []. Example: my_list = [1, 2, 3]
- Tuple: An immutable, ordered collection of items. Defined with parentheses (). Example: my_tuple = (1, 2, 3)

## What is the purpose of the None data type in Python?
- None represents the absence of a value or a null value. It is often used to signify that a variable has no value or to initialize a variable.

## How can you check the data type of a variable?
- You can use the type() function to check the data type of a variable. 
``` python
x = 5
print(type(x))  # Output: <class 'int'>
```

## What is a set and how is it different from a list?
- Set: An unordered collection of unique items. Defined with curly braces {}. Example: my_set = {1, 2, 3}
- List: An ordered collection of items that can contain duplicates. Defined with square brackets []. Example: my_list = [1, 2, 2, 3]

## What is a complex number and how do you create one in Python?
- A complex number has a real part and an imaginary part. You can create a complex number using the complex() function or by using the j notation. Example:
``` python
z = complex(2, 3)  # Output: (2+3j)
z = 2 + 3j  # Output: (2+3j)
```

## Explain the str data type and give an example.
- The str data type represents a sequence of characters (a string). Strings are immutable and can be defined using single, double, or triple quotes. Example:
``` python
my_string = "Hello, World!"
```

## What are the Boolean values in Python and how are they used?
- The Boolean data type has two values: True and False. They are used for conditional statements and logical operations. Example:
``` python
a = True
b = False
if a:
    print("a is True")
else:
    print("a is False")
```

---

# print()
## How do you print a string in Python?
``` python
print("Hello, world!")
```

## How do you print multiple items in one line?
``` python
print("Hello", "world", 123)
```

## How do you print a variable's value?
``` python
x = 42
print(x)
```

## How do you include variables within a string?
``` python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Using f-strings
```

## How do you format strings using the format() method?
``` python
name = "Alice"
age = 30
print("{} is {} years old.".format(name, age))
```

## How do you print numbers with specific formatting (e.g., two decimal places)?
``` python
pi = 3.14159
print(f"{pi:.2f}")
```

## How do you align text (left, right, center) within a fixed width?
``` python
text = "hello"
print(f"{text:<10}")  # Left-aligned
print(f"{text:>10}")  # Right-aligned
print(f"{text:^10}")  # Centered
```

## How do you print with a custom separator between items?
``` python
print("A", "B", "C", sep="-")
```

## How do you print without a newline at the end?
``` python
print("Hello", end=" ")
print("world!")
```

## How do you print special characters (e.g., newline, tab)?
``` python
print("Line 1\nLine 2")
print("Column 1\tColumn 2")
```

## How do you print the contents of a list or dictionary?
``` python
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}
print(my_list)
print(my_dict)
```

## How do you print an error message to stderr?
``` python
import sys
print("Error occurred!", file=sys.stderr)
```

## How do you print raw strings (ignoring escape sequences)?
``` python
print(r"Raw string with \n no escape sequences")
```

## How do you suppress the automatic space added between items?
``` python
print("A", "B", "C", sep="")
```

---
# Function

Certainly! Here are 10 basic questions about functions in Python, along with their answers:

## What is a function in Python?
A function in Python is a block of reusable code that performs a specific task. It can take inputs, process them, and return a result.

## How do you define a function in Python?
You define a function using the `def` keyword followed by the function name and parentheses containing any parameters. The function body is indented.
```python
def greet(name):
    print(f"Hello, {name}!")
```

## How do you call (invoke) a function in Python?
You call a function by writing its name followed by parentheses containing any arguments.
```python
greet("Alice")
```

## What is the purpose of the `return` statement in a function?
The `return` statement is used to exit a function and optionally pass an expression back to the caller.
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5
```

## How do you define a function with default parameter values?
You can assign default values to parameters in the function definition. These parameters are optional when calling the function.
```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, World!
greet("Alice") # Output: Hello, Alice!
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
Use `*args` to allow the function to accept any number of positional arguments.

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

## What is a lambda function in Python?
A lambda function is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

---
