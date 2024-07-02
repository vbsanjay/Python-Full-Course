# Dictionary

## What is Dictionary?
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered, changeable and do not allow duplicates.
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

## What does the keys(), values(), and items() methods do?
- keys() returns a view object that displays a list of all the keys in the dictionary.
- values() returns a view object that displays a list of all the values in the dictionary.
- items() returns a view object that displays a list of all the key-value pairs in the dictionary.
    ```python
    keys = my_dict.keys()       # Output: dict_keys(['name', 'email'])
    values = my_dict.values()   # Output: dict_values(['Alice', 'alice@example.com'])
    items = my_dict.items()     # Output: dict_items([('name', 'Alice'), ('email', 'al
    ```

## What is view object?
- A view object in Python is a dynamic view on the dictionary's keys, values, or items, meaning that when the dictionary changes, the view reflects these changes. 
- View objects are lightweight and provide a live view into the dictionary's keys, values, or items.
- They are returned by the dictionary methods keys(), values(), and items().
- Keys and items view objects support set operations such as union, intersection, and difference.
- View objects can be iterated over in a loop.
- View objects do not support indexing or slicing.
    ```python
    my_dict = {"a": 1, "b": 2}
    keys_view = my_dict.keys()  # dict_keys(['a', 'b'])
    my_dict["c"] = 3
    print(keys_view)  # dict_keys(['a', 'b', 'c'])
    ```

## How do you merge two dictionaries?
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # dict1 is now {'a': 1, 'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}  # {'a': 1, 'b': 3, 'c': 4}
```

## How do you check if a key exists in a dictionary?
```python
if "name" in my_dict:
    print("Key 'name' exists.")
```

## What is the defaultdict from the collections module?
- A defaultdict is like a regular dictionary but with a default value for non-existing keys.
    ```python
    from collections import defaultdict
    dd = defaultdict(int)
    dd["a"] += 1
    # Output: defaultdict(<class 'int'>, {'a': 1})
    ```

## How do you copy a dictionary?
- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
- There are ways to make a copy, one way is to use the built-in Dictionary method copy().
    ```python
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)
    ```
## Common Pitfalls in Python Dictionaries

1. **Mutable Default Arguments**:
   - **Pitfall**: Using a mutable default argument (like a dictionary) in a function definition.
   - **Example**:
     ```python
     def add_to_dict(key, value, my_dict={}):
         my_dict[key] = value
         return my_dict
     
     print(add_to_dict('a', 1))  # {'a': 1}
     print(add_to_dict('b', 2))  # {'a': 1, 'b': 2} - unexpected!
     ```
   - **Solution**: Use `None` as the default argument and initialize inside the function.
     ```python
     def add_to_dict(key, value, my_dict=None):
         if my_dict is None:
             my_dict = {}
         my_dict[key] = value
         return my_dict
     
     print(add_to_dict('a', 1))  # {'a': 1}
     print(add_to_dict('b', 2))  # {'b': 2}
     ```

2. **Key Errors**:
   - **Pitfall**: Accessing a non-existent key directly raises a `KeyError`.
   - **Example**:
     ```python
     my_dict = {'a': 1}
     print(my_dict['b'])  # KeyError
     ```
   - **Solution**: Use the `.get()` method or check for the key's existence.
     ```python
     print(my_dict.get('b'))  # None
     print(my_dict.get('b', 0))  # 0
     
     if 'b' in my_dict:
         print(my_dict['b'])
     ```

3. **Unintended Overwrites**:
   - **Pitfall**: Assigning a new value to an existing key unintentionally overwrites the previous value.
   - **Example**:
     ```python
     my_dict = {'a': 1, 'b': 2}
     my_dict['a'] = 3
     print(my_dict)  # {'a': 3, 'b': 2}
     ```
   - **Solution**: Ensure you want to overwrite the value or check if the key already exists.
     ```python
     if 'a' not in my_dict:
         my_dict['a'] = 3
     ```

4. **Dictionary Size Changes During Iteration**:
   - **Pitfall**: Modifying a dictionary while iterating over it raises a `RuntimeError`.
   - **Example**:
     ```python
     my_dict = {'a': 1, 'b': 2}
     for key in my_dict:
         if key == 'a':
             del my_dict[key]  # RuntimeError
     ```
   - **Solution**: Iterate over a copy of the dictionary's keys or use dictionary comprehensions.
     ```python
     for key in list(my_dict.keys()):
         if key == 'a':
             del my_dict[key]
     
     # or
     my_dict = {k: v for k, v in my_dict.items() if k != 'a'}
     ```

5. **Using Unhashable Types as Keys**:
   - **Pitfall**: Using lists or other unhashable types as dictionary keys raises a `TypeError`.
   - **Example**:
     ```python
     my_dict = {[1, 2]: 'value'}  # TypeError
     ```
   - **Solution**: Use only hashable types (e.g., strings, numbers, tuples) as keys.
     ```python
     my_dict = {(1, 2): 'value'}
     ```

## Best Practices for Using Python Dictionaries

1. **Use Dictionary Comprehensions**:
   - Simplifies dictionary creation and makes the code more readable.
   - Example:
     ```python
     squares = {x: x*x for x in range(6)}
     print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
     ```

2. **Use `.get()` for Default Values**:
   - Safely access dictionary values with a default return value if the key doesn't exist.
   - Example:
     ```python
     my_dict = {'a': 1}
     print(my_dict.get('b', 0))  # 0
     ```

3. **Leverage `.setdefault()` for Initialization**:
   - Initialize and update dictionary values in a single operation.
   - Example:
     ```python
     my_dict = {}
     my_dict.setdefault('a', []).append(1)
     print(my_dict)  # {'a': [1]}
     ```

4. **Use `defaultdict` for Default Values**:
   - Automatically initializes missing keys with default values.
   - Example:
     ```python
     from collections import defaultdict
     my_dict = defaultdict(list)
     my_dict['a'].append(1)
     print(my_dict)  # defaultdict(<class 'list'>, {'a': [1]})
     ```

5. **Iterate with `.items()`**:
   - Iterate over key-value pairs efficiently.
   - Example:
     ```python
     my_dict = {'a': 1, 'b': 2}
     for key, value in my_dict.items():
         print(f'{key}: {value}')
     ```

6. **Merge Dictionaries with `|` Operator**:
   - Merging dictionaries in Python 3.9+.
   - Example:
     ```python
     dict1 = {'a': 1}
     dict2 = {'b': 2}
     merged_dict = dict1 | dict2
     print(merged_dict)  # {'a': 1, 'b': 2}
     ```

7. **Use Dictionary Views for Efficient Lookups**:
   - Use `.keys()`, `.values()`, and `.items()` for efficient membership tests and iterations.
   - Example:
     ```python
     my_dict = {'a': 1, 'b': 2}
     if 'a' in my_dict.keys():
         print('Key exists')
     ```
