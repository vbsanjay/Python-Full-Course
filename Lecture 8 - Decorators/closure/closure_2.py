# Write a program to find average of numbers provided by the user so far

# APPROACH 1: Using class

class Average:
    def __init__(self) -> None:
        self.numbers = []

    def avg(self, number: int) -> int:
        self.numbers.append(number)
        total_sum = sum(self.numbers)
        count = len(self.numbers)
        return total_sum / count

calc_avg = Average()
res = calc_avg.avg(1)
res = calc_avg.avg(7)
print("using class:",res)

# APPROACH 2: Using closure

def average():
    numbers = []
    def calc(number):
        numbers.append(number)
        total_sum = sum(numbers)
        count = len(numbers)
        return total_sum / count
    return calc

avg = average()
avg(1)
res = avg(9)
print("using closure:",res)

# APPROACH 3: Using closure optimized

def average():
    total_sum = 0
    count = 0
    def calc(number):
        nonlocal total_sum
        nonlocal count
        total_sum += number
        count += 1
        return total_sum / count
    return calc

avg = average()
avg(1)
res = avg(19)
print("using closure(optimized):",res)

# My observation is, when a class need to perform only one function, closure can be considered

# Write a closure to calculate the number of times a function is called

c = dict()
def adder(a: int, b: int) -> int:
    return a + b

def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return a // b

def counter(func, counters):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[func.__name__] = count
        return func(*args, **kwargs)

    return inner


counter_add = counter(adder,c)
print(counter_add(1,2))
print(counter_add(4,2))
print(counter_add(7,6))
counter_mult = counter(mult,c)
print(counter_mult(2,5))
print(counter_mult(10,2))

print(c)

print(div(10,2)) # 5
print(c) # {'adder': 3, 'mult': 2}
# now you can have the name of variable as same a function and observe how it works

div = counter(div,c)

# now we 'div' is used but with the extra functionality provided by the closure 

print(div(10,2)) # 5
print(c) # {'adder': 3, 'mult': 2, 'div': 1}
