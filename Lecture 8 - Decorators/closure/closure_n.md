# Closure
## What is a closure in Python?
- A closure is a function object that remembers and accesses variables from its outer function, even after the outer function has completed execution. 
- **Key Components of a Closure**
    - Nested Function: A function defined inside another function.
    - Free Variables: Variables from the enclosing scope that are referenced in the nested function.
    - Returning the Nested Function: The outer function returns the nested function, allowing it to be called later.
- Use Cases: Closures are used for maintaining state, implementing decorators, and creating factory functions.

## How Closures Work
1. Definition of Closure:
A closure is a function object that has access to variables in its lexical scope, even when the function is called outside that scope.

2. Lexical Scoping:
Python uses lexical scoping, which means that the scope of a variable is determined by its position in the source code.

3. Nested Functions:
Closures typically involve nested functions - an inner function defined inside an outer function.

4. Free Variables:
Variables from the outer function that are used in the inner function are called "free variables".

5. Creation of Closure:
When the inner function is defined, Python creates a closure by:
   a. Identifying the free variables used in the inner function.
   b. Creating cell objects for each free variable.
   c. Storing references to these cell objects in the inner function's `__closure__` attribute.

6. Cell Objects:
   a. Cell objects are containers that hold references to the values of free variables.
   b. They allow both reading and writing of the free variables.
   c. Cell objects are shared between the inner function and the enclosing scope.

7. Function Objects:
   a. In Python, functions are first-class objects.
   b. When a function is created, Python creates a function object.
   c. This object includes the function's code, name, and other attributes, including `__closure__`.

8. The `__closure__` Attribute:
   a. This is a tuple of cell objects for the function's free variables.
   b. If the function is not a closure, `__closure__` is None.

9. Returning Inner Function:
The outer function typically returns the inner function, without calling it.

10. Execution of Closure:
When the returned inner function is later called:
    a. Python looks up the values of free variables through the cell objects in `__closure__`.
    b. This allows access to the original values, even if the outer function has completed execution.

11. Variable Lifetime:
Free variables referenced by the closure are not destroyed when the outer function finishes. They remain alive as long as the closure exists.

12. Garbage Collection:
Python's garbage collector keeps the free variables alive as long as they are referenced by any existing closure.

13. Mutability in Closures:
   a. If a free variable is mutable (like a list), changes to it inside the closure affect the original object.
   b. For immutable types (like integers), reassignment inside the closure creates a new local variable, not affecting the original.

14. Late Binding:
Closures in Python use late binding. The values of variables in the closure are looked up at the time the inner function is called, not when it's defined.

15. Practical Uses:
Closures are used for data hiding, implementing decorators, and creating function factories.

Here's an example that illustrates these concepts:

```python
def outer(x):
    y = 20  # This will be a free variable

    def inner():
        print(f"x: {x}, y: {y}")  # x and y are free variables
        
    print(f"Inner function's closure: {inner.__closure__}")
    return inner

closure = outer(10)
print(f"Closure's __closure__ attribute: {closure.__closure__}")
print(f"First cell's contents: {closure.__closure__[0].cell_contents}")
print(f"Second cell's contents: {closure.__closure__[1].cell_contents}")
closure()  # This will print "x: 10, y: 20"
```

This example demonstrates the creation and use of a closure, including the role of cell objects and the `__closure__` attribute.

## Key characteristics of closure
- They are nested functions.
- They have access to variables from their enclosing scope.
- They maintain references to those variables, allowing them to be used after the outer function has finished execution.

## Closure and free variable
- A **closure** in Python is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. This allows the function to use those variables later, making it a "closed-over" function. 
- A **free variable** is a variable used in the function that is not defined within it, but in an outer scope. Closures keep references to these free variables. Here's an example:

```python
def outer(x):
    def inner(y):
        return x + y  # 'x' is a free variable for 'inner'
    return inner

closure_example = outer(10)
print(closure_example(5))  # Outputs 15
```
- Free variables are specifically related to nested functions where the inner function uses variables from the outer function's scope.

# Closure and Cell Object
## What is Cell Object?
- Python uses cell objects to store references to variables captured from the enclosing scope.
- These cell objects are part of the function object’s __closure__ attribute.
```python
def outer():
    a = 'hello'
    def inner():
        print(a)
    return inner
```
- Here, `inner()` is a closure because it "closes over" the variable `a` from its enclosing scope. 
- When `outer()` is called and returns `inner`, Python creates a special object called a "cell" that keeps `a` alive, even after `outer()` finishes executing.
- This allows `inner()` to retain access to `a` when it's called later.

## Closure concept in Python step by step
1. Definition of Closure:
A closure is a function object that has access to variables in its lexical scope, even when the function is called outside that scope.

2. Lexical Scoping:
Python uses lexical scoping, which means that the scope of a variable is determined by its position in the source code.

3. Nested Functions:
Closures typically involve nested functions - an inner function defined inside an outer function.

4. Free Variables:
Variables from the outer function that are used in the inner function are called "free variables".

5. Creation of Closure:
When the inner function is defined, Python creates a closure by:
   a. Identifying the free variables used in the inner function.
   b. Creating cell objects for each free variable.
   c. Storing references to these cell objects in the inner function's `__closure__` attribute.

6. Cell Objects:
   a. Cell objects are containers that hold references to the values of free variables.
   b. They allow both reading and writing of the free variables.
   c. Cell objects are shared between the inner function and the enclosing scope.

7. Function Objects:
   a. In Python, functions are first-class objects.
   b. When a function is created, Python creates a function object.
   c. This object includes the function's code, name, and other attributes, including `__closure__`.

8. The `__closure__` Attribute:
   a. This is a tuple of cell objects for the function's free variables.
   b. If the function is not a closure, `__closure__` is None.

9. Returning Inner Function:
The outer function typically returns the inner function, without calling it.

10. Execution of Closure:
When the returned inner function is later called:
    a. Python looks up the values of free variables through the cell objects in `__closure__`.
    b. This allows access to the original values, even if the outer function has completed execution.

11. Variable Lifetime:
Free variables referenced by the closure are not destroyed when the outer function finishes. They remain alive as long as the closure exists.

12. Garbage Collection:
Python's garbage collector keeps the free variables alive as long as they are referenced by any existing closure.

13. Mutability in Closures:
   a. If a free variable is mutable (like a list), changes to it inside the closure affect the original object.
   b. For immutable types (like integers), reassignment inside the closure creates a new local variable, not affecting the original.

14. Late Binding:
Closures in Python use late binding. The values of variables in the closure are looked up at the time the inner function is called, not when it's defined.

15. Practical Uses:
Closures are used for data hiding, implementing decorators, and creating function factories.

Here's an example that illustrates these concepts:

```python
def outer(x):
    y = 20  # This will be a free variable

    def inner():
        print(f"x: {x}, y: {y}")  # x and y are free variables
        
    print(f"Inner function's closure: {inner.__closure__}")
    return inner

closure = outer(10)
print(f"Closure's __closure__ attribute: {closure.__closure__}")
print(f"First cell's contents: {closure.__closure__[0].cell_contents}")
print(f"Second cell's contents: {closure.__closure__[1].cell_contents}")
closure()  # This will print "x: 10, y: 20"
```
 

