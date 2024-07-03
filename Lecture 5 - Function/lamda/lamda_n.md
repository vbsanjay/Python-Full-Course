# Lamda

## Syntax
lambda arguments : expression

## What is a lambda function in Python?
A lambda function is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

## Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```

## How do lambda functions differ from regular functions in Python?
- Lambda functions are syntactically restricted to a single expression. 
- They are also anonymous, meaning they don't need a name. 
- Regular functions are defined using the def keyword and can contain multiple expressions and statements.

## When should you use lambda functions in Python?
Lambda functions are useful when you need a simple function for a short period of time, such as for use in higher-order functions like map(), filter(), and sorted(), or for inline use where defining a full function would be overkill.

## Can lambda functions have multiple lines?
No, lambda functions are restricted to a single expression. If you need multi-line functionality, you should define a regular function.


