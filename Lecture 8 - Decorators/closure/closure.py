def outer(x):
    y = 20
    def inner():
        print(f"\nx:{x}, y:{y}")
        print(f"\nid(x):{hex(id(x))}, id(y):{hex(id(y))}") # the memory address of this x and y are stored in the cell object
    print(f"\nInner function's objects's __closure_ attribute = \n {inner.__closure__}") # tuple of cell object
    return inner

closure = outer(10)
print(f"\nclosure function object = {closure}")
print(f"\nClosure's __closure__ attribute: {closure.__closure__}")
print(f"\nFirst cell's contents: {closure.__closure__[0].cell_contents}")
print(f"\nSecond cell's contents: {closure.__closure__[1].cell_contents}")

closure()