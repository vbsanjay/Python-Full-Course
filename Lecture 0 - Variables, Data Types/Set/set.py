# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry"}
# Access Items
for x in thisset:
  print(x)

# Add Items
thisset.add("orange")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry", "mango"}
mylist = ["kiwi", "orange", "mango"]

# thisset = thisset + mylist TypeError: unsupported operand type(s) for +: 'set' and 'list'
thisset.update(mylist)
print(thisset) # {'banana', 'apple', 'orange', 'mango', 'kiwi', 'cherry'}

thisset.remove("banana")
print(thisset) 

set1 = {1,2,3}
set2 = {"apple", "orange", 1}

set3 = set1.union(set2) # The union() method returns a new set with all items from both sets.
print(set3) # {1, 2, 3, 'apple', 'orange'}

# You can use the | operator instead of the union() method, and you will get the same result.
# set3 = set1 | set2

# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) # The intersection() method will return a new set, that only contains the items that are present in both sets.
print(set3) # {'apple'}

# You can use the & operator instead of the intersection() method, and you will get the same result.
# set3 = set1 & set2

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1) # {'apple'}

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3) # {False, 1, 'apple'}

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) # {'cherry', 'banana'}

# You can use the - operator instead of the difference() method, and you will get the same result.
# set3 = set1 - set2

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
# set1.difference_update(set2)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # {'banana', 'google', 'microsoft', 'cherry'}

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# set3 = set1 ^ set2

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
# set1.symmetric_difference_update(set2)
