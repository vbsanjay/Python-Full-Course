# Type Conversion

## What is type conversion in Python?
- Type conversion in Python refers to the process of converting one data type to another. There are two types of type conversion: implicit (automatic) and explicit (manual). 
- Implicit conversion is handled automatically by Python, whereas explicit conversion requires the use of built-in functions.

## How can you convert a list of strings to a list of integers in Python?
- You can use a list comprehension with the `int()` function. For example:
  ```python
  str_list = ["1", "2", "3"]
  int_list = [int(i) for i in str_list]
  print(int_list)  # Output: [1, 2, 3]
  ```

## What is the `ord()` function used for?
- The `ord()` function converts a single character string to its corresponding ASCII/Unicode code point. For example:
  ```python
  char = 'A'
  code_point = ord(char)
  print(code_point)  # Output: 65
  ```

## What is the `chr()` function used for?
- The `chr()` function converts an integer representing a Unicode code point to its corresponding character. For example:
  ```python
  code_point = 65
  char = chr(code_point)
  print(char)  # Output: 'A'
  ```

## Explain how Python handles type conversion in expressions involving multiple types.
- Python performs implicit type conversion in expressions to ensure that operations are conducted on compatible types. For example, in mixed-type expressions, Python promotes the type with lower precision to the type with higher precision. For example:
  ```python
  result = 5 + 3.5  # 5 is implicitly converted to 5.0
  print(result)  # Output: 8.5
  print(type(result))  # Output: <class 'float'>
  ```

## What is the hierarchy of types from lower to higher precision in Python?
- Implicit type conversion follows the principle of converting a lower precision type to a higher precision type to prevent data loss. Here is the hierarchy of types from lower to higher precision in Python:

1. **Integer (`int`)**
2. **Floating-point (`float`)**
3. **Complex (`complex`)**

- Implicit type conversion occurs in the following order:
    - **Integer (`int`)** -> **Floating-point (`float`)** -> **Complex (`complex`)**

### Examples

1. **Integer to Float Conversion**
    ```python
    int_num = 5
    float_num = 2.5
    result = int_num + float_num  # int_num is implicitly converted to float
    print(result)  # Output: 7.5
    print(type(result))  # Output: <class 'float'>
    ```

2. **Integer to Complex Conversion**
    ```python
    int_num = 5
    complex_num = 3 + 4j
    result = int_num + complex_num  # int_num is implicitly converted to complex
    print(result)  # Output: (8+4j)
    print(type(result))  # Output: <class 'complex'>
    ```

3. **Float to Complex Conversion**
    ```python
    float_num = 2.5
    complex_num = 1 + 3j
    result = float_num + complex_num  # float_num is implicitly converted to complex
    print(result)  # Output: (3.5+3j)
    print(type(result))  # Output: <class 'complex'>
    ```

## Describe a situation where type conversion might lead to data loss.
- Converting a float to an integer leads to data loss because the decimal part is truncated. For example:
  ```python
  f = 3.9
  num = int(f)
  print(num)  # Output: 3
  ```

## How can you implement a custom type conversion method in a Python class?
- You can define methods like `__int__()`, `__float__()`, and `__str__()` in your class. For example:
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value

      def __int__(self):
          return int(self.value)

      def __float__(self):
          return float(self.value)

      def __str__(self):
          return str(self.value)

  obj = MyClass(42.5)
  print(int(obj))    # Output: 42
  print(float(obj))  # Output: 42.5
  print(str(obj))    # Output: '42.5'
  ```

## Write a function that takes a list of mixed data types and returns a list where all numbers are converted to floats and all other types remain unchanged.
- Example implementation:
  ```python
  def convert_to_floats(mixed_list):
      result = []
      for item in mixed_list:
          if isinstance(item, (int, float)):
              result.append(float(item))
          else:
              result.append(item)
      return result

  mixed_list = [1, 'hello', 3.5, 2]
  converted_list = convert_to_floats(mixed_list)
  print(converted_list)  # Output: [1.0, 'hello', 3.5, 2.0]
  ```

## Explain how type conversion works when dealing with complex numbers in Python.
- Python supports complex numbers with the `complex` type. The real and imaginary parts of a complex number can be converted to floats. For example:
  ```python
  c = 3 + 4j
  real_part = c.real
  imag_part = c.imag
  print(real_part)  # Output: 3.0
  print(imag_part)  # Output: 4.0
  ```

## What is the purpose of the `float.is_integer()` method?
- The `float.is_integer()` method checks if a float is an integer value (i.e., has no fractional part). For example:
  ```python
  num = 4.0
  print(num.is_integer())  # Output: True

  num = 4.5
  print(num.is_integer())  # Output: False
  ```

## You are given a list of numbers as strings. Write a function to convert this list to a list of integers, handling any invalid input gracefully.
- Example implementation:
  ```python
  def convert_to_integers(str_list):
      result = []
      for s in str_list:
          try:
              result.append(int(s))
          except ValueError:
              continue
      return result

  str_list = ["10", "20", "abc", "30"]
  int_list = convert_to_integers(str_list)
  print(int_list)  # Output: [10, 20, 30]
  ```

## What is a `ValueError` in Python and when does it occur?
- A `ValueError` occurs when a function receives an argument of the right type but an inappropriate value. For example, converting a non-numeric string to an integer will raise a `ValueError`.
- **Example:**
  ```python
  int('abc')  # Raises ValueError: invalid literal for int() with base 10: 'abc'
  ```

## What is a `TypeError` in Python and when does it occur?
- A `TypeError` occurs when an operation or function is applied to an object of an inappropriate type. For example, passing `None` to the `int` function will raise a `TypeError`.
- **Example:**
  ```python
  int(None)  # Raises TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
  ```