# Reduce

## What does the `reduce()` function do in Python?
- The `reduce()` function applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument, to reduce the iterable to a single value.

## What is the syntax of the `reduce()` function?
- The syntax is `reduce(func, iterable[, initial])`, where `func` is the function to apply, `iterable` is the collection of elements, and `initial` is an optional value that serves as the starting point.

## How does the `reduce()` function handle the initial value?
- If the `initial` value is provided, it becomes the first argument to `func`, and the first element of `iterable` becomes the second argument. If `initial` is not provided, the first element of `iterable` becomes the first argument to `func`, and the second element becomes the second argument.

## Explain with an example how `reduce()` works without an initial value.
- ```python
   from functools import reduce
   numbers = [1, 2, 3, 4, 5]
   result = reduce(lambda x, y: x + y, numbers)
   print(result)  # Output: 15
   ```

## Explain with an example how `reduce()` works with an initial value.
- ```python
   from functools import reduce
   numbers = [1, 2, 3, 4, 5]
   result = reduce(lambda x, y: x + y, numbers, 10)
   print(result)  # Output: 25
   ```

## What happens if the iterable passed to `reduce()` is empty and no initial value is provided?
- If the iterable is empty and no initial value is provided, `reduce()` raises a `TypeError`.

## What are the advantages of using `reduce()`?
- The `reduce()` function provides a concise and readable way to perform cumulative operations on an iterable. It simplifies code that requires the combination of all elements into a single value.

## How can you use `reduce()` to implement a custom `sum()` function?
- ```python
   from functools import reduce
   def custom_sum(x, y):
       return x + y
   numbers = [5, 8, 10, 20, 25]
   result = reduce(custom_sum, numbers)
   print(result)  # Output: 68
   ```

## What are the requirements for the function passed to `reduce()`?
- The function passed to `reduce()` must take two arguments and return a single value.

## Can you use `reduce()` with built-in functions? Provide an example.
- Yes, `reduce()` can be used with built-in functions. For example:
  ```python
  from functools import reduce
  numbers = [1, 2, 3, 4, 5]
  result = reduce(lambda x, y: x * y, numbers)
  print(result)  # Output: 120
  ```