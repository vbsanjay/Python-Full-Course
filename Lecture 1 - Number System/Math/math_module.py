import math

# sqrt()
print("sqrt(25):", math.sqrt(25))  # Output: 5.0
print("sqrt(2):", math.sqrt(2))    # Output: 1.4142135623730951

# sin(), cos(), tan()
print("sin(pi / 2):", math.sin(math.pi / 2))  # Output: 1.0
print("cos(0):", math.cos(0))                 # Output: 1.0
print("tan(pi / 4):", math.tan(math.pi / 4))  # Output: 1.0

# pi
radius = 5
circumference = 2 * math.pi * radius
print("Circumference:", circumference)  # Output: 31.41592653589793

# e
print("exp(1):", math.exp(1))        # Output: 2.718281828459045
print("log(e):", math.log(math.e))   # Output: 1.0

# Practical application: Pythagorean theorem
a, b = 3, 4
hypotenuse = math.sqrt(a**2 + b**2)
print("Hypotenuse:", hypotenuse)  # Output: 5.0

# Angles in degrees
angle_a = math.degrees(math.atan(a / b))
print("Angle opposite side a:", angle_a)  # Output: 36.86989764584402

angle_b = math.degrees(math.atan(b / a))
print("Angle opposite side b:", angle_b)  # Output: 53.13010235415599

# Finding the GCD
a = 15
b = 5
print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(b, a)) 

#  Finding the factorial of the number
a = 5
print("The factorial of 5 is : ", end="")
print(math.factorial(a))

# Finding the ceiling and the floor value
a = 2.3
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a)) 

# Finding the Logarithm
print ("The value of log 2 with base 3 is : ", end="") 
print (math.log(2,3)) 
print ("The value of log2 of 16 is : ", end="") 
print (math.log2(16)) 
print ("The value of log10 of 10000 is : ", end="") 
print (math.log10(10000))

