a = 0
b = 10

try:
    a/b
except ZeroDivisionError:
    print("can't divide by 0")
finally:
    print("finally division is done")