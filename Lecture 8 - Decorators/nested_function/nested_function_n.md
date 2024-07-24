# Nested Function

## What is a nested function in Python, and why are they useful?
- A nested function is a function defined inside another function.
- They are useful because:
    - They encapsulate logic that is only relevant within the enclosing function.
    - They allow for the creation of closures.

## Declaring and Calling a Nested Function in Python
- Define the outer function.
- Define the inner (nested) function inside the outer function.
- Call the inner function from within the outer function.
- Call the outer function from outside.

## Can nested functions access variables from the outer function?
- Yes, nested functions can access and modify variables from the enclosing function's scope.

## What is a closure in Python?
- A closure is a function object that remembers and accesses variables from its outer function, even after the outer function has completed execution. 
- **Key Components of a Closure**
    - Nested Function: A function defined inside another function.
    - Free Variables: Variables from the enclosing scope that are referenced in the nested function.
    - Returning the Nested Function: The outer function returns the nested function, allowing it to be called later.
- Use Cases: Closures are used for maintaining state, implementing decorators, and creating factory functions.

## How Closures Work
- When a nested function references a variable from its enclosing scope, that variable is preserved in a closure. This allows the nested function to access those variables even after the outer function has exited.

## nonlocal Keyword
- Used within nested functions to modify variables in the outer function's scope.

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

## What happens to the variable 'a' when the outer function finishes executing, and how can the inner function still access it?
- When the outer function finishes executing, its local scope is normally destroyed. However, because `a` is referenced in the closure of the inner function, it's not actually deleted. Instead:
    1. Python creates a cell object that contains `a` and its value.
    2. This cell is attached to the inner function's closure.
    3. The outer function's local variable `a` ceases to exist, but the value it pointed to ('hello') is preserved in the cell.
    4. When the inner function is later called, it accesses `a` through this cell in its closure.
This mechanism allows the inner function to "remember" and use the value of `a`, even though the outer function's execution has completed.

## Do both the outer and inner function's 'a' point to the same memory address, and what happens to these references over time?

Yes, initially both the outer function's `a` and the inner function's reference to `a` point to the same memory address containing 'hello'. However, their lifecycle differs:

1. While the outer function is executing, its local `a` and the inner function's closure both point to 'hello'.
2. When the outer function finishes, its local `a` variable is destroyed.
3. The inner function's closure retains a reference to the cell containing 'hello'.
4. When the inner function is later called, it still accesses the same 'hello' string through its closure.

The key point is that the outer function's local variable `a` doesn't exist after the function completes, but the value it pointed to is preserved for the inner function's use via the closure mechanism.
