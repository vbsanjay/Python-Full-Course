# Write a class so that its objects are iterable
# To make a class iterable implement __iter__ and __next__ special functions

class TopTen:

    def __init__(self) -> None:
        self.number = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 10:
            self.number += 1
            return self.number
        else:
            raise StopIteration
        

it = TopTen()

for i in it:
    print(i)

it = TopTen()

while True:
    try:
        print(it.__next__())
    except StopIteration:
        break

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self): 
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1
                       
# Driver code
if __name__ == '__main__' :
    a, b = 2, 5
    c1 = Counter(a, b)
    c2 = Counter(a, b)
    
    # Way 1-to print the range without iter()
    print ("Print the range without iter()")
    
    for i in c1:
        print ("Eating more Pizzas, counting ", i, end ="\n")
    
    print ("\nPrint the range using iter()\n")
    
