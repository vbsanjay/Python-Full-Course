from functools import reduce

# reduce: to find the sum of all the elements in the list
ls = [1,2,3,4]
# ls = [] # type error is seen

print(reduce(lambda x, y: x + y, ls, 50))
