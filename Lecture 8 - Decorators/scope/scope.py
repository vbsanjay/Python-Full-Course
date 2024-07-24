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
print("'a' is been modified in func3. a:", a)
# func4() # this line throws run time error since during compile time python know there is 'a' existing in local scope.
# during run time 'a' it sees a does not have any value in it.