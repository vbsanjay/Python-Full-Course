s = "hello world"

# capitalize first letter
s = s.capitalize()
print(s)

# make s a title
s = s.title()
print(s)

# upper case
s = s.upper()
print(s)

# lower case
s = s.lower()
print(s)

# check if digit
print(s.isdigit())

# insert a letter in the string
s = s[:5] + " my" + s[5:]
print(s)

# change a letter in the string
s = s[:5] + " to" + s[8:]
print(s)
s = s.replace(" to", " my")
print(s)

# delete a letter in the string
s = s.replace(" my", "")
print(s)

# swap 2 letter in a string
s = list(s)
print(s)
s[0], s[4] = s[4], s[0]
s = "".join(s)
print(s)

