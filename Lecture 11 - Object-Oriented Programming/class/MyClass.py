class MyClass:
    c = 20
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_a(self):
        print(self.a)

    def print_b(self):
        print(self.b)
    

myObj = MyClass(10,2,3)
MyClass.print_a(myObj)
print(myObj.c, MyClass.c)
myObj.x = 10

print(myObj.x)