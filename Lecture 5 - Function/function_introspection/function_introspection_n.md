# Function Introspection

## What is a first-class object in Python?
- A first-class object is an entity that supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.
- In Python, functions are first-class objects, meaning you can:
  - Assign them to variables.
  - Pass them as arguments to other functions.
  - Return them from functions.
  - Store them in data structures like lists or dictionaries.

## What is a second-class object in Python?
- Second-class objects in Python typically refer to entities that have restrictions on how they can be used compared to first-class objects. In Python, this distinction is not formal or widely recognized, but informally:
  - Second-class objects might refer to types like dictionaries, lists, sets, and frozensets, which have limitations such as being mutable or not directly supporting certain operations like being used as keys in dictionaries.

## What are the types of objects available in Python?
- **First-Class Objects:**
  - Functions
  - Integers
  - Floats
  - Strings
  - Tuples
  - Classes
  - Instances (Objects of a class)
  
- **Second-Class Objects:**
  - Dictionaries
  - Lists
  - Sets
  - Frozensets

## What is function introspection in Python?
- Function introspection in Python refers to the ability to examine the properties of functions at runtime.
- It allows you to gather information about functions, such as their name, documentation, default argument values, and more.

## How can you retrieve the name of a function in Python?
- Use the `__name__` attribute of the function.

## How can you access the docstring of a function?
- Use the `__doc__` attribute of the function.

## How can you get the default argument values of a function?
- Use the `__defaults__` attribute of the function.

## What attribute provides the type annotations of a function?
- The `__annotations__` attribute.

## How can you retrieve the source code of a function?
- Use the `inspect.getsource()` function from the `inspect` module.

## How can you obtain the signature of a function, including its parameters?
- Use the `inspect.signature()` function from the `inspect` module.

## What is the `Signature` object in the `inspect` module?
- The `Signature` object provides details about a function's parameters and return annotations.

## How can you list all the members of a function object?
- Use the `inspect.getmembers()` function from the `inspect` module.

## How do you retrieve the docstring of a function using the `inspect` module?
- Use the `inspect.getdoc()` function.

## How can you get information about the compiled function body?
- Use the `__code__` attribute of the function.

## Provide an example of function introspection using the `inspect` module.
- Example:
  ```python
  import inspect
  
  def example_function(a: int, b: int = 5) -> int:
      """This is an example function that adds two numbers."""
      return a + b

  # Using function attributes
  print("Function name:", example_function.__name__)
  print("Docstring:", example_function.__doc__)
  print("Annotations:", example_function.__annotations__)
  print("Defaults:", example_function.__defaults__)

  # Using the inspect module
  sig = inspect.signature(example_function)
  print("Signature:", sig)
  for param in sig.parameters.values():
      print(param.name, param.default, param.annotation)

  source = inspect.getsource(example_function)
  print("Source code:\n", source)
  ```

## How can function introspection be useful in debugging and logging?
- It allows you to dynamically examine functions, making it easier to understand their behavior.
- It helps in generating detailed logs and debug information.

## Which is better to find information about a function: default dunder attributes or the `inspect` module?
- **Inspect Module:**
    - Provides comprehensive functions (`inspect.signature()`, `inspect.getsource()`, etc.) designed specifically for function introspection.
    - Offers structured and readable outputs, enhancing ease of use compared to manually accessing dunder attributes.
    - Allows for programmatically gathering various details about functions, beneficial for debugging, logging, and dynamic analysis.

- **Default Dunder Attributes:**
    - Provides basic information such as `__name__`, `__doc__`, etc.
    - Accessible directly from the function object but may require additional processing for detailed introspection needs.

In summary, the **`inspect` module** is generally preferred for detailed and comprehensive function introspection in Python.