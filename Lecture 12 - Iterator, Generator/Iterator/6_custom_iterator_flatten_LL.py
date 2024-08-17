from collections.abc import Iterable

class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration

def flatten(nested_list):
    return FlattenIterator(nested_list)

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
flat_iter = flatten(nested_list)

print(list(flat_iter))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# You can also use it in a for loop
for item in flatten(nested_list):
    print(item, end=' ')  # Output: 1 2 3 4 5 6 7 8