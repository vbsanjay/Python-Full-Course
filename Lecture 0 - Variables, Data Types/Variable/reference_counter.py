import sys
p = [1,2,3]
# The function sys.getrefcount(p) includes the temporary reference created by passing p to the function itself, so it will always be at least 1 more than the actual number of references to the object.
print("reference count of p:",sys.getrefcount(p))

# ctypes.c_long.from_address(id(q)).value reads the reference count directly from the memory address of the object q.
# This method does not create a temporary reference, so it reflects the actual number of references to the object.
q = p
import ctypes
print("reference count of p:", ctypes.c_long.from_address(id(q)).value)

# funciton to count reference counter
def ref_count(address):
    return ctypes.c_long.from_address(address).value

x = [4,5,6]
print( "\nreference count of x:", ref_count(id(x)) )
y = x
print( "reference count of y:", ref_count(id(y)) )
z = x
print( "reference count of z:", ref_count(id(z)) )

z = None
print( "\nreference count of z:", ref_count(id(x)) )
y = None
print( "reference count of y:", ref_count(id(x)) )

x_id = id(x)
x = None
print( "\nreference count of x_id:", ref_count(x_id) )
 
print( "\nreference count of x:", ref_count(id(x)) )
print( "reference count of y:", ref_count(id(y)) )
print( "reference count of z:", ref_count(id(z)) )
