# Map

## What is the `map()` function in Python and what is its purpose?
- The `map()` function in Python applies a given function to all the items in an input list (or iterable) and returns an iterator (map object) that yields the results.

## What is the syntax of the `map()` function?
- The syntax is `map(func, *iterables)`, where `func` is the function to be applied, and `*iterables` is one or more iterables whose elements will be passed as arguments to `func`.

## What is the difference in the return type of `map()` between Python 2 and Python 3?
- In Python 2, `map()` returns a list. In Python 3, `map()` returns a map object, which is a generator object. To convert it to a list, you need to use `list(map(func, *iterables))`.

## How does the `map()` function handle multiple iterables?
- If multiple iterables are passed, `map()` stops when the shortest iterable is exhausted. It pairs each element from the iterables with the corresponding argument of the function.

## Explain with an example how `map()` works with a single iterable.
- ```python
   my_pets = ['alfred', 'tabitha', 'william', 'arla']
   result = list(map(str.upper, my_pets))
   print(result)  # Output: ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
   ```

## Explain with an example how `map()` works with multiple iterables.
- ```python
   circle_areas = [3.56773, 5.57668, 4.00923, 56.24232, 9.01344, 8.98732]
   result = list(map(round, circle_areas, range(1, 7)))
   print(result)  # Output: [3.6, 5.58, 4.009, 56.2423, 9.01344, 8.98732]
   ```

## What happens if the iterables passed to `map()` have different lengths?
- If the iterables have different lengths, `map()` stops iterating when the shortest iterable is exhausted.

## How can you convert the result of `map()` to a list in Python 3?
- You can convert the result of `map()` to a list by using the `list()` function: `list(map(func, *iterables))`.

## Write a custom zip() function using `map()`.
- ```python
   my_strings = ['a', 'b', 'c', 'd']
   my_numbers = [1, 2, 3, 4]
   result = list(map(lambda x, y: (x, y), my_strings, my_numbers))
   print(result)  # Output: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
   ```

## What are the advantages of using `map()` over a traditional for loop?
- `map()` provides a more concise and readable way to apply a function to a list of elements. It can be more efficient as it avoids the need to explicitly write the iteration logic, and it can be combined with other functional programming tools like `filter()` and `reduce()`.

# Zip

## What is the purpose of the `zip()` function in Python?
- The `zip()` function takes a number of iterables and creates tuples containing elements from each iterable at the same position.

## What does the `zip()` function return in Python 3?
- In Python 3, the `zip()` function returns a generator object.

## How can you convert the result of the `zip()` function to a list?
- You can convert the result of the `zip()` function to a list by using the `list()` function: `list(zip(iterable1, iterable2, ...))`.

## Explain how the `zip()` function works with an example.
- The `zip()` function pairs elements from multiple iterables:
  ```python
  iter1 = [1, 2, 3]
  iter2 = ['a', 'b', 'c']
  result = list(zip(iter1, iter2))
  print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
  ```

## What happens if the iterables passed to the `zip()` function have different lengths?
- If the iterables have different lengths, the `zip()` function stops creating tuples when the shortest iterable is exhausted.

## How can you implement a custom `zip()` function using the `map()` function?
- You can implement a custom `zip()` function using the `map()` function and a lambda function to create tuples:
  ```python
  iter1 = [1, 2, 3]
  iter2 = ['a', 'b', 'c']
  result = list(map(lambda x, y: (x, y), iter1, iter2))
  print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
  ```

## What are the advantages of using the `zip()` function?
- The `zip()` function provides a concise and readable way to combine multiple iterables into tuples. It simplifies the process of pairing elements from multiple sequences.

## Can you use the `zip()` function with more than two iterables? Provide an example.
- Yes, the `zip()` function can be used with more than two iterables:
  ```python
  iter1 = [1, 2, 3]
  iter2 = ['a', 'b', 'c']
  iter3 = [True, False, True]
  result = list(zip(iter1, iter2, iter3))
  print(result)  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
  ```