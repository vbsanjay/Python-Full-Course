
# Data types

## What are the basic data types in Python?
- The basic data types in Python are:
    - Integers: int 
    - Floating-point numbers: float 
    - Complex numbers: complex 
    - Strings: str 
    - Booleans: bool 
    - NoneType: None

## How can you check the data type of a variable?
- You can use the type() function to check the data type of a variable. 
``` python
x = 5
print(type(x))  # Output: <class 'int'>
```

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