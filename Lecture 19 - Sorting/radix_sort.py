def radx_count_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    # count the frequency of a digit
    for num in arr:
        index = num // exp % 10
        count[index] += 1

    # prefix frequency sum which determine the position of the number in the result array
    for i in range(1,10):
        count[i] += count[i-1]

    # generate the sorted array based on the prefix sum frequency array
    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radx_sort(arr):
    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        radx_count_sort(arr, exp)
        exp *= 10

nums = [100,245,50,105,78,2670,20,945,4]
radx_sort(nums)
print(nums)