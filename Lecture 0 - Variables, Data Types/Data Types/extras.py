'''
This file covers the extra topics
'''

# locals() and globals(): these function provies access to the local and global symbol table
print("\nGlobal variables using globals():", globals())
def example_function():
    local_variable = 20
    print("Local variables using locals():", locals())

example_function()


# String interning
s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # Output: True

t1 = (1,2,3)
t2 = (1,2,3)
print(t1 is t2) # Output: True

x = 300
y = 300
print(x is y)  # Output: True

z1 =[1,2,3]
z2 =[1,2,3]
print(z1 is z2)  # Output: False

a = 20.12
b = 20.12
print(a is b) # Output: True