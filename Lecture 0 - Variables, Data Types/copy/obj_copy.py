# shallow copy
import copy
ls = [1,2,3]
ls_copy = copy.copy(ls)
ls_copy[1] = -1
print(ls)
print(ls_copy)

# Tricky part: you may think any change in objects contained by ls_copy should reflect in ls. but this is not the case here
# in the above example ls_copy contains immutable objects so any change in ls_copy will not change the ls object
original_list = [1, [2, 3], 4]

shallow_copied_list = copy.copy(original_list)

# Modify the original list to demonstrate shallow copy behavior
original_list[1][0] = 'X'

print("Original list:", original_list)  # [1, ['X', 3], 4]
print("Shallow copied list:", shallow_copied_list)  # [1, ['X', 3], 4]

# here the list [2.3] within original_list is mutable any changes within in will affect both original and copied list

# deep copy

deep_ls = [1,2,3]

deep_ls_copy = copy.deepcopy(deep_ls)

deep_ls_copy[1] = -1

print(deep_ls)
print(deep_ls_copy)

original_list = [1, [2, 3], 4]

deep_copied_list = copy.deepcopy(original_list)

# Modify the original list to demonstrate deep copy behavior
original_list[1][0] = 'Y'

print("Original list:", original_list)  # [1, ['Y', 3], 4]
print("Deep copied list:", deep_copied_list)  # [1, [2, 3], 4]