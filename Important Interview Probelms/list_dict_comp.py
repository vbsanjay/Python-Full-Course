# create a list and dict comprehension

ls = [x for x in range(5)]
print(ls)

dic = {x: x**2 for x in range(5)}
print(dic)


print("----------")
print(dir())
print("----------")
print(locals())
print("----------")
print(globals())

class MyClass:
    """ hey """
    def __init__(self):
        self.value = 5

obj = MyClass()
print("----------")
print(obj.__dict__) 


help(obj) 
print(MyClass.__doc__ )