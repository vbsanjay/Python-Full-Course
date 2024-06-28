# syntax : [expression for item in iterable]

ls = [i for i in range(0,5)]

print(ls)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [num for row in matrix for num in row]

print(flat_list)

