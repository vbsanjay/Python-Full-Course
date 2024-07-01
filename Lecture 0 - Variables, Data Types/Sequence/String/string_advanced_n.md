# String: Advanced

## How does Python handle Unicode and encoding in strings?
- Python 3 strings are Unicode by default, which means they can store characters from any language.
- Encoding is the process of converting a Unicode string into a byte sequence (e.g., UTF-8).
  ```python
  unicode_str = 'Hello, 世界'
  encoded_str = unicode_str.encode('utf-8')  # Convert to bytes
  decoded_str = encoded_str.decode('utf-8')  # Convert back to string
  ```

## What is the difference between `str` and `bytes` in Python?
- **`str`:** Represents a sequence of Unicode characters.
- **`bytes`:** Represents a sequence of byte (8-bit) values.
  ```python
  str1 = 'Hello'
  bytes1 = b'Hello'  # Note the 'b' prefix
  ```

- Converting between `str` and `bytes`:
  ```python
  str1 = 'Hello'
  bytes1 = str1.encode('utf-8')
  str2 = bytes1.decode('utf-8')
  ```

## Explain the concept of string interning in Python.
- **String Interning:** A method of storing only one copy of each distinct string value, which must be immutable.
- **Usage:** Interning is used to save memory and speed up string comparisons. Python automatically interns certain strings (like identifiers and strings with only ASCII letters) but not all strings.
- **Manual Interning:** You can manually intern a string using the `sys.intern()` function:
  ```python
  import sys
  a = sys.intern('example')
  b = sys.intern('example')
  a is b  # True
  ```

## What is the `StringIO` module and how is it used in Python?
- **StringIO:** A module in the `io` library that provides an in-memory file-like object for reading and writing strings.
- **Usage:** Useful for manipulating string data with file-like operations.
  ```python
  from io import StringIO

  str_io = StringIO()
  str_io.write("Hello, World!")
  str_io.seek(0)
  print(str_io.read())  # 'Hello, World!'
  ```

## How can you format numbers inside a string in Python (e.g., formatting floating-point numbers to two decimal places)?
- **Using f-strings:**
  ```python
  num = 123.456789
  formatted_str = f"{num:.2f}"
  print(formatted_str)  # '123.46'
  ```
- **Using `format()` Method:**
  ```python
  formatted_str = "{:.2f}".format(num)
  print(formatted_str)  # '123.46'
  ```

## What is string interpolation, and how is it implemented in Python?
- **String Interpolation:** The process of embedding expressions within string literals.
- **Implementation in Python:**
  - **f-strings:** Embed expressions directly in the string.
    ```python
    name = "Alice"
    greeting = f"Hello, {name}!"
    ```
  - **`format()` Method:** Use placeholders `{}` in the string.
    ```python
    greeting = "Hello, {}!".format(name)
    ```

## What are some common performance considerations when working with strings in Python?
- **Avoiding `+` for Concatenation:** Using `+` in loops can lead to quadratic time complexity. Use `join()` instead.
  ```python
  parts = ["Hello", "World", "Again"]
  combined = " ".join(parts)  # Efficient
  ```
- **String Interning:** Use interning for frequently-used strings to save memory and speed up comparisons.
- **Lazy Evaluation:** Use generators for processing large text data.

## Explain how to use regular expressions with strings in Python.
- **Regular Expressions:** Patterns used for matching, searching, and manipulating text.
- **Using `re` Module:**
  ```python
  import re

  pattern = r"\bHello\b"
  text = "Hello World! Hello again!"
  matches = re.findall(pattern, text)
  print(matches)  # ['Hello', 'Hello']
  ```

## How do you handle large strings or large-scale text processing in Python efficiently?
- **Using Generators:** Process large texts line by line to avoid loading the entire text into memory.
  ```python
  def read_large_file(file_path):
      with open(file_path, 'r') as file:
          for line in file:
              yield line.strip()

  for line in read_large_file("large_text.txt"):
      print(line)
  ```
- **Memory Mapping:** Use `mmap` for large files to access portions of the file as needed.

## How can you escape special characters in a string in Python?
- **Using Backslash (`\`):**
  ```python
  escaped_str = "He said, \"Hello, World!\""
  print(escaped_str)  # He said, "Hello, World!"
  ```
- **Using `repr()` Function:** For a string representation that includes escape characters.
  ```python
  raw_str = repr("Hello\nWorld")
  print(raw_str)  # 'Hello\nWorld'
  ```

## What is the difference between raw strings and regular strings in Python?
- **Regular Strings:** Interpret escape sequences like `\n` (newline) and `\t` (tab).
  ```python
  regular_str = "Hello\nWorld"
  print(regular_str)  # Hello
                     # World
  ```
- **Raw Strings:** Treat backslashes as literal characters, useful for regex patterns and file paths.
  ```python
  raw_str = r"Hello\nWorld"
  print(raw_str)  # Hello\nWorld
  ```