
# Task: I should not alter the div function. I need to implement a should always greater than b
def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    print(a/b)

div(5,10)
