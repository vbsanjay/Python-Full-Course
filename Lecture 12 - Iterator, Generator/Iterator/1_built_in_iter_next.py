# Using inbuilt iter() and __next__() 

# iter() function returns an iterator when we pass the iterable object in the parameter
nums = [1,2,3,4]
# next(ls) # this will throw an error: 'list' object is not an iterator
it = iter(nums)
print(next(it), 'from', next)
print(it.__next__(), 'from', it.__next__)

for num in nums:
    print(num, 'from the "for" loop`s iterator' )

for num in it:
    print(num, 'from', it.__next__ )

# Ouput
# 1 from <built-in function next>
# 2 from <method-wrapper '__next__' of list_iterator object at 0x1073079d0>
# 1 from the "for" loop`s iterator
# 2 from the "for" loop`s iterator
# 3 from the "for" loop`s iterator
# 4 from the "for" loop`s iterator
# 3 from <method-wrapper '__next__' of list_iterator object at 0x1073079d0>
# 4 from <method-wrapper '__next__' of list_iterator object at 0x1073079d0>


# Other way to iterate using while loop
it = iter(nums)

while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break

# output
# 1
# 2
# 3
# 4
