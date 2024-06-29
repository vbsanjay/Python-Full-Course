a = 10
b = a

# Memory address of a and b are same
print("id of a:", id(a))
print("id of a:", id(b))

x = 20
y = 20

# Memory address of x and y are same
print("id of x:", id(x))
print("id of y:", id(y))

q = 30
w = 40

# Memory address of q and w are not same
print("id of q:", id(q))
print("id of w:", id(w))