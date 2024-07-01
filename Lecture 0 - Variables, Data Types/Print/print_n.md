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