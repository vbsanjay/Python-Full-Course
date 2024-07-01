print("Arithmetic Operators")
print("2 + 3 = ", end=" ")  # addition
print(2 + 3)
print("2 - 3 = ", end=" ")  # subtracting
print(2 - 3)
print("2 * 3 = ", end=" ")  # multiplication
print(2 * 3)
print("5 % 2 = ", end=" ")  # modulus
print(5 % 2)
print("5 ** 2 = ", end=" ")  # exponentiation
print(5 ** 2)
print("4 / 2 = ", end=" ")  # True division
print(4 / 2)
print("4 // 2 = ", end=" ")  # Floor division
print(4 // 2)
print("3 / 2 = ", end=" ")  # True division
print(3 / 2)
print("3 // 2 = ", end=" ")  # Floor division
print(3 // 2)
print()

print("Comparison Operators")
result = (5 == 3)  # Equal to (==)
print("5 == 3", result)
result = (5 != 3)  # Not equal to (!=)
print("5 != 3", result)
result = (5 > 3)  # Greater than (>)
print("5 > 3", result)
result = (5 < 3)  # Less than (<)
print("5 < 3", result)
result = (5 >= 3)  # Greater than or equal to (>=)
print("5 >= 3", result)
result = (5 <= 3)  # Less than or equal to (<=)
print("5 <= 3", result)
print()

print("Logical Operators")
result = (True and False)  # Logical AND (and)
print("True and False", result)
result = (True or False)  # Logical OR (or)
print("True or False", result)
result = not True  # Logical NOT (not)
print("not True", result)
print()

print("Bitwise Operators")
result = 5 & 3  # Bitwise AND
print("5 & 3 =", result)
result = 5 | 3  # Bitwise OR
print("5 | 3 =", result)
result = ~5  # Bitwise NOT
print("~5 =", result)
result = 5 ^ 3  # Bitwise XOR
print("5 ^ 3 =", result)
result = 5 << 1  # Bitwise left shift
print("5 << 1 =", result)
result = 5 >> 1  # Bitwise right shift
print("5 >> 1 =", result)
print()

print("Assignment Operators")
x = 5
x += 3  # equivalent to x = x + 3
x -= 3  # equivalent to x = x - 3
x *= 3  # equivalent to x = x * 3
x /= 3  # equivalent to x = x / 3
x //= 3  # equivalent to x = x // 3
x %= 3  # equivalent to x = x % 3
x **= 3  # equivalent to x = x ** 3

x = 5
x &= 3  # equivalent to x = x & 3
x |= 3  # equivalent to x = x | 3
x ^= 3  # equivalent to x = x ^ 3
x <<= 3  # equivalent to x = x << 3
x >>= 3  # equivalent to x = x >> 3
print()

print("Membership Operators")
result = 'a' in 'apple'  # In (in)
print("'a' in 'apple'", result)
result = 'b' not in 'apple'  # Not in (not in)
print("'b' not in 'apple'", result)
print()

print("Identity Operators")
x = [1, 2, 3]
y = x
result = (x is y)  # Is (is)
print("x is y", result)

x = [1, 2, 3]
y = [1, 2, 3]
result = (x is not y)  # Is not (is not)
print("x is not y", result)