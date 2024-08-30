class CountSort:

    def __call__(self, nums):
        max_value = max(nums)
        freq_counter = [0] * (max_value + 1)
        res_arr = []
        for num in nums:
            freq_counter[num] += 1

        for index, value in enumerate(freq_counter):
            if freq_counter[index]:
                res_arr.extend([index] * value)
        
        nums = res_arr


nums = [1,2,5,10,7,2,20,15,4]

mysort = CountSort()
mysort(nums)
print(nums)

