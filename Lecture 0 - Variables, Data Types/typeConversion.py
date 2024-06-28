# type conversion
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print("before type conversion 2 input strings are added. x + y =", z)  # output is String
z = int(x) + int(y)
print("after type conversion 2 integers were added. x + y =", z)  # output is String

# nested function with type conversion
a = int(input("What's a? "))
b = int(input("What's b? "))
print("a + b using nested function and type conversion. a + b =", a + b)

# float
i = float(input("What's i? "))
j = int(input("What's j? "))
print("adding using float i + j =", i + j)

# round
k = round(i / j)
# k = round(i / j, 2)
print("rounding the i / j =", k)
print(f"rounding the i / j using f string {i/j:.2f}")

# Numeric formatting
n = 100000
print(f"Numeric formatting {n:,}")
