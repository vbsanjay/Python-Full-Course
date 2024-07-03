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
