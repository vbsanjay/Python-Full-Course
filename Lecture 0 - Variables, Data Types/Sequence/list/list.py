# Create a list
ls = [1,2,3,4,6,7]

# Insert in a list at the start
ls.insert(0,0)
print(ls)
# [0, 1, 2, 3, 4, 5, 6, 7]

# Insert in a list at the end
ls.append(8)
print(ls)

# Insert in a list at the middle
ls.insert(5, 5)
print(ls)

# Access a element form the list
a = ls[0]
print(a)
b = ls[-1]
print(b)

# Accessing a range of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Accessing range of negative index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)