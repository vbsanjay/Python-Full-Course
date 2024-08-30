def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1  # Calculate the correct index for the current element
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]  # Swap to place the element at the correct index
        else:
            i += 1  # Move to the next element if the current element is already at its correct index

# Example usage
arr = [3, 1, 5, 4, 2]
cyclic_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 4, 5]
