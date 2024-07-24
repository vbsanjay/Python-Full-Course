a = 10

def func1():
    print("In func1, 'a' exisitng outside function is printed"
          "since it can't find 'a' within in the function. a:", a)

def func2():
    a = 100
    print("In func2, masking is performed on 'a'. "
          "'a' does not change it global value. a:", a)

def func3():
    global a
    print("In func3, 'a' is refered as global so printing global value of 'a'. a:",a)
    a = 20

def func4():
    print("In func4,'a' printing throws error. a:", a)
    a = 100

func1()
func2()
func3()
print("'a' is been modified in func3. a:", a,"\n")
# func4() # this line throws run time error since during compile time python know there is 'a' existing in local scope.
# during run time 'a' it sees a does not have any value in it.

#non-local variable

# scenario 1:
def outer_func():
    y = 20 # this is non-local variable to inner_func(). 
    # A non-local variable is neither a local variable of an inner function nor a global variable.
    def inner_func():
        print("value of non-local variable y:",y)
    inner_func()

outer_func()

# scenario 2:
x = 10
def outer_func():
    def inner_func():
        print("value of global variable x:",x)
    inner_func()

outer_func()

# scenario 3:
def outer_func():
    y = 20 # this is non-local variable to inner_func(). 
    # A non-local variable is neither a local variable of an inner function nor a global variable.
    def inner_func():
        y = 10
        print("value of masked y in inner function:",y)
    inner_func()
    print("value of y in outer function:",y)

outer_func()

# value of masked y in inner function: 10
# value of y in outer function: 20
# value of y does not change in the non-local scope.

# scenario 3:
# just like 'global' keyword we have 'nonlocal' keyword
def outer_func():
    y = 20 # this is non-local variable to inner_func(). 
    # A non-local variable is neither a local variable of an inner function nor a global variable.
    def inner_func():
        nonlocal y
        y = 10 
        print("value of y (not masked, instead mentioned nonlocal) in inner function:",y)
    inner_func()
    print("value of y in outer function is changed:",y)

outer_func()
# value of y (not masked, instead mentioned nonlocal) in inner function: 10
# value of y in outer function is changed: 10

i = 100
def outer_func():
    i = 10
    def inner_func1():
        nonlocal i
        i = 20
        def inner_func2():
            nonlocal i
            i = 30
            print('\ni from inner function2. i:', i)
        inner_func2()
        print('i from inner function1. i:', i)
    inner_func1()
    print('i from outer function. i:', i)

outer_func()
print('i from global state. i:', i)

# **important** key point to remember: 
# in a multi level nested function variable with nonlocal key word points to the neartest outer non-local variable
# to understand the above run the below code
u = 'peace'
def outer_func():
    u = 'hello'
    def inner_func1():
        def inner_func2():
            nonlocal u
            u = 'sanjay'
            print('\nu from inner function2. u:', u)
        inner_func2()
        print('u from inner function1. u:', u)
    inner_func1()
    print('u from outer function. u:', u)

outer_func()
print('u from global state. u:', u)

# for inner most function inner_func2() the variable in outer_func and inner_func are non local variable