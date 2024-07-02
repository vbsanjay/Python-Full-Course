x = 10  # 1010 in binary
y = 4   # 0100 in binary

# & AND	Sets each bit to 1 if both bits are 1
and_result = x & y  # 1010 & 0100 = 0000
print(f"x & y = {and_result}")

# |	OR	Sets each bit to 1 if one of two bits is 1
or_result = x | y  # 1010 | 0100 = 1110
print(f"x | y = {or_result}")

# ^	XOR	Sets each bit to 1 if only one of two bits is 1
xor_result = x ^ y  # 1010 ^ 0100 = 1110
print(f"x ^ y = {xor_result}")

# ~	NOT	Inverts all the bits
not_result = ~x  # ~1010 = -(1010 + 1) = -1011 = -11
print(f"~x = {not_result}")

# << Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
left_shift_result = x << 2  # 1010 << 2 = 101000 = 40
print(f"x << 2 = {left_shift_result}")

# >> Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
right_shift_result = x >> 2  # 1010 >> 2 = 0010 = 2
print(f"x >> 2 = {right_shift_result}")
