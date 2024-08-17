# Implement a custom iterator for a range function.

class RangeFunc:
    
    def __init__(self, start, end=None, step = 1):
        if end == None:
            end = start
            start = 0

        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        return self

    def __next__(self):
        val = self.current
        if (self.step > 0 and self.current <= self.end) or (self.step < 0 and self.current >= self.end):
            self.current  += self.step
            return val
        else:
            raise StopIteration


it = RangeFunc(1,10,2) # Adjust the range and see the change in output

for i in it:
    print(i)

# Output
# 1
# 3
# 5
# 7
# 9
