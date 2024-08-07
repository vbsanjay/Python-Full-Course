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