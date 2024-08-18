# how iterator is used in map function
x = [1,2,3,4,5,6,7,8,9]
y = map(lambda i: i ** 2, x) # y is an iterator returned by map
print(type(y))

print("1st time")
for i in y:
    print(i)

print("2nd time")

for i in y:
    print(i)

# The reason the second iteration over it does not print anything 
# is that the map function returns an iterator, and iterators in Python are "one-time use." Once an iterator is exhausted, it cannot be reused or reset.


# range is not an iterator. range function returns range object which we need to change it as an iterator

x = range(1, 10)
it = iter(x)
print(type(it))
print(it.__next__())

for i in it:
    print(i)

