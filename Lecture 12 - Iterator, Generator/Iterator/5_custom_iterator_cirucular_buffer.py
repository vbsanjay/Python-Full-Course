class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0
        self.temp = 0

    def add(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        if self.count < self.size:
            self.count += 1
        else:
            self.head = (self.head + 1) % self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.temp:
            self.temp = 0
            raise StopIteration
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.temp += 1
        return item

    def __len__(self):
        return self.count
    
it = CircularBuffer(4)
it.add(1)
it.add(2)
it.add(3)
it.add(4)
it.add(5)
it.add(6)

for i in it:
    print(i)

print("2nd time")
for i in it:
    print(i)
print("2nd time done")