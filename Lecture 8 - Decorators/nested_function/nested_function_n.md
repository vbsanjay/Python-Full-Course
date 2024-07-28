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

## nonlocal Keyword
- Used within nested functions to modify variables in the outer function's scope.
