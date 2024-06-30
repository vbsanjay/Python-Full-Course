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
