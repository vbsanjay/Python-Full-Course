def outer(x):
    y = 20
    def inner():
        print(f"\nx:{x}, y:{y}")
        print(f"\nid(x):{hex(id(x))}, id(y):{hex(id(y))}") # the memory address of this x and y are stored in the cell object
    print(f"\nInner function's objects's __closure_ attribute = \n {inner.__closure__}") # tuple of cell object
    return inner

closure = outer(10)
print(f"\nclosure function object = {closure}")
print(f"\n__closure__: {closure.__closure__}")
print(f"\nFirst cell's contents: {closure.__closure__[0].cell_contents}")
print(f"\nSecond cell's contents: {closure.__closure__[1].cell_contents}")

closure()

# Inner function's objects's __closure_ attribute = 
#  (<cell at 0x10e7d3fd0: int object at 0x10e3e1608>, <cell at 0x10e7d3e20: int object at 0x10e3e1748>)

# closure function object = <function outer.<locals>.inner at 0x10e6b0540>

# __closure__: (<cell at 0x10e7d3fd0: int object at 0x10e3e1608>, <cell at 0x10e7d3e20: int object at 0x10e3e1748>)

# First cell's contents: 10

# Second cell's contents: 20

# x:10, y:20

# id(x):0x10e3e1608, id(y):0x10e3e1748
print("\n--------------------------------------------------------")

# Create a simple closure that print hello world

def outer():
    string = 'hello'
    def inner():
        print(f"\n{string} world")
    
    return inner

closure = outer()
print(f"\nclosure function object = {closure}")
print(f"\n__closure__: {closure.__closure__}")
closure()

# closure function object = <function outer.<locals>.inner at 0x10e77a160>

# __closure__: (<cell at 0x10e7d3d60: str object at 0x10e7c7070>,)

# hello world
print("\n--------------------------------------------------------")

# Create a closure with a list as free variable

def outer():
    ls = [1,2,3,4]
    def inner():
        for i in range(4):
            print(ls[i], end = " ")
    return inner

closure = outer()
print(f"\nclosure function object = {closure}")
print(f"\n__closure__: {closure.__closure__}\n")
closure()

# closure function object = <function outer.<locals>.inner at 0x10e7ccf40>

# __closure__: (<cell at 0x10e7d3fd0: list object at 0x10e725ac0>,)

# 1 2 3 4 
print("\n--------------------------------------------------------")

# Create a closure and explore integer interning, string interning and list

def outer():
    x = 1234
    print(f"\n{hex(id(x))}")
    def inner():
        nonlocal x
        x = 1234
        print(hex(id(x)))
    return inner

closure = outer()
print(f"\nclosure function object = {closure}")
print(f"\n__closure__: {closure.__closure__}\n")
closure()

# 0x10e633eb0

# closure function object = <function outer.<locals>.inner at 0x10e6b0540>

# __closure__: (<cell at 0x10e7d3e20: int object at 0x10e633eb0>,)

# 0x10e633eb0
print("\n--------------------------------------------------------")

# Create 2 closure within a single outer function

def outer():
    z = "Hey "
    print(f"\n{z}")

    def inner1():
        nonlocal z
        z = z + "I am "
        return z
    
    def inner2():
        nonlocal z
        z = z + "Sanjay"
        return z

    return inner1, inner2

f1, f2 = outer()
print(f"\nf1.__closure__: {f1.__closure__}")
print(f"\nf2.__closure__: {f2.__closure__}")

print((f"\n{f1()}"))
print(f"\nf1.__closure__: {f1.__closure__}")
print(f"\nf2.__closure__: {f2.__closure__}")

print((f"\n{f2()}"))
print(f"\nf1.__closure__: {f1.__closure__}")
print(f"\nf2.__closure__: {f2.__closure__}")

# Hey 

# f1.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c73b0>,)

# f2.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c73b0>,)

# Hey I am 

# f1.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c7df0>,)

# f2.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c7df0>,)

# Hey I am Sanjay

# f1.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c7a30>,)

# f2.__closure__: (<cell at 0x10e7d3fd0: str object at 0x10e7c7a30>,)
print("\n--------------------------------------------------------")

# Explore how variables are shared across scopes
# Below is bit tricky exercise
# Problem statement: arr should store list of function which add 2 number. n is auto generated from the for loop and x is user input
# each function in list should have value of n incremented as 0,1,2,....,n

# Approach 1: without closure - FAIL
arr = []
for n in range(3):
    arr.append(lambda x: x + n)

print(f"\nlist containing function: {arr}")
print(f"\narr[0].__closure__ = {arr[0].__closure__}\n")
# arr[0].__closure__ = None. No closure is creates since n is a global scope here and no free variable attained from enclosing scope
print(arr[0](10)) # expected output:10  actual output:12

# Approach 2: with closure - FAIL
def adder():
    arr = []
    for n in range(3):
        arr.append(lambda x: x + n)
    print(f"\nlist containing function: {arr}")
    print(f"\narr[0].__closure__ = {arr[0].__closure__}\n")
    # closure is created since n is local variable to outer function and n is free variable in inner lambda function
    return arr
created_arr = adder()
print(created_arr[0](10)) # expected output:10  actual output:12


# Approach 3: with closure and default variable - PASS
def adder():
    arr = []
    for n in range(3):
        arr.append(lambda x, y=n: x + y)
    print(f"\nlist containing function: {arr}")
    print(f"\narr[0].__closure__ = {arr[0].__closure__}\n")
    # No closure is created since no free variable is carried from enclosing scope
    # y = n, y is a local variable to inner lambda function. y is assigned to n at the created time of the function rather than run time
    return arr
created_arr = adder()
print(created_arr[0](10)) # expected output:10  actual output:10

