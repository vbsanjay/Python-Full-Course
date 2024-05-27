x = input("What's x? ")
y = input("What's y? ")

z = x + y

print("before type conversion 2 input strings are added", z)  # output is String

z = int(x) + int(y)
print("after type conversion 2 integers were added", z)  # output is String


