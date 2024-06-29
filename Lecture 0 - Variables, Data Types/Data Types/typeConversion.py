# type conversion
x = "5"
y = "8"
z = x + y
print("before type conversion 2 input strings are added. x + y =", z)  # output is String
z = int(x) + int(y)
print("after type conversion 2 integers were added. x + y =", z)  # output is Integer

# nested function with type conversion
a = int(input("What's a? "))
b = int(input("What's b? "))
print("a + b using nested function and type conversion. a + b =", a + b)

# float
i = float("12")
j = int("12")
print("adding using float i + j =", i + j) #implicit type conversion

# int()
x =  int(3.14)
print("x =", x)

