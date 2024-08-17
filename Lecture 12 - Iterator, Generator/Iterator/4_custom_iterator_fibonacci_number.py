class Fibonacci_number:
    first = 0
    second = 1
    count = 1

    def __init__(self, number):
        self.number = number
        if self.number < 0:
            self.number *= -1 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count <= 2:
            temp = self.count
            self.count += 1
            return temp - 1
        elif self.count == self.number:
            raise StopIteration
        else:
            val = self.first + self.second
            self.first, self.second = self.second, val
            self.count += 1
            return val

numbers = Fibonacci_number(10)

for i in numbers:
    print(i)

print(len(numbers))


# here is an intersting learning. using yield in below code where we don't use __next__()

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def add(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        if self.count < self.size:
            self.count += 1
        else:
            self.head = (self.head + 1) % self.size

    def __iter__(self):
        idx = self.head
        num = 0
        while num < self.count:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num += 1

    def __len__(self):
        return self.count
    


# Create a circular buffer of size 5
cb = CircularBuffer(5)

# Add some items
for i in range(7):
    cb.add(i)

# Iterate over the buffer
print("Buffer contents:", list(cb))  # Output: [2, 3, 4, 5, 6]

# Add more items
cb.add(7)
cb.add(8)

# Iterate again
print("Buffer contents after adding more items:", list(cb))  # Output: [4, 5, 6, 7, 8]

# Check the length
print("Number of items in buffer:", len(cb))  # Output: 5


# Why next() is not used here:
# In this implementation, we don't explicitly use next() because we're creating an iterable, not an iterator
# The __iter__ method defines how to iterate over our CircularBuffer, but it doesn't make the CircularBuffer itself an iterator.

# How iter() is enough to iterate:
# The __iter__ method in our CircularBuffer class is actually returning a generator. 
# When you define a method with yield statements, Python automatically turns it into a generator function.
# When called, a generator function returns a generator object, which is itself an iterator.

# Here's what's happening behind the scenes:
# When you use the CircularBuffer in a for loop or call iter() on it, Python calls the __iter__ method.
# The __iter__ method returns a generator object.
# This generator object is an iterator, so it has its own __next__ method.
# The for loop (or whatever is using the iterator) calls next() on this generator object repeatedly to get values.