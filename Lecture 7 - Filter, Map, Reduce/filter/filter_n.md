# Filter

## What does the `filter()` function do in Python?
- The `filter()` function passes each element in the iterable through a function that returns a boolean value. It "filters" out elements that return `False` and returns only those that return `True`.

## What is the syntax of the `filter()` function?
- The syntax is `filter(func, iterable)`, where `func` is the function that returns a boolean value, and `iterable` is the collection of elements to be filtered.

## How does `filter()` differ from `map()` in terms of function requirements and the number of iterables?
- Unlike `map()`, `filter()` requires the function to return a boolean value. Additionally, `filter()` only requires one iterable, whereas `map()` can take multiple iterables.

## What does `filter()` return in Python 3?
- In Python 3, `filter()` returns a filter object, which is an iterator. To get a list, you need to convert it using `list(filter(func, iterable))`.

## Explain with an example how `filter()` works with a single iterable.
- ```python
   scores = [55, 90, 78, 65, 89, 76, 91, 82, 71, 60]
   result = list(filter(lambda x: x > 75, scores))
   print(result)  # Output: [90, 78, 89, 76, 91, 82]
   ```

## What is the requirement for the function passed to `filter()`?
- The function passed to `filter()` must return a boolean type (True or False).

## What happens if the function passed to `filter()` does not return a boolean type?
- If the function does not return a boolean type, `filter()` simply returns the iterable passed to it.

## How can you use `filter()` to detect palindromes in a list of words?
- ```python
   words = ('madam', 'racecar', 'apple', 'banana', 'anutforajaroftuna')
   result = list(filter(lambda word: word == word[::-1], words))
   print(result)  # Output: ['madam', 'racecar', 'anutforajaroftuna']
   ```

## What are the advantages of using `filter()` over a traditional for loop?
- `filter()` provides a more concise and readable way to apply a condition to a list of elements. It can be more efficient as it avoids the need to explicitly write the iteration and condition-checking logic.

## Can `filter()` be used with built-in functions? Provide an example.
- Yes, `filter()` can be used with built-in functions. For example:
  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  result = list(filter(lambda x: x % 2 == 0, numbers))
  print(result)  # Output: [2, 4, 6, 8, 10]
  ```