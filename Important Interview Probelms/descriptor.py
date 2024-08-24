class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return f"Getting {self.name}"

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")

    def __delete__(self, instance):
        print(f"Deleting {self.name}")

class MyClass:
    attr = Descriptor("attr")

obj = MyClass()
print(obj.attr)  # Calls Descriptor.__get__()
obj.attr = 10    # Calls Descriptor.__set__()
print(obj.attr)
del obj.attr     # Calls Descriptor.__delete__()
