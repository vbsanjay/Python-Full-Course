def fibonacci(n):
    first = 0
    yield 0
    second = 1
    yield 1
    for i in range(n-2):
        yield first + second
        first, second = second, first + second
    

for i in fibonacci(5):
    print(i)

x = fibonacci(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))