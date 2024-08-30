class Selection_sort:
    
    def __call__(self,nums):
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            
            nums[i],nums[min_index] = nums[min_index], nums[i]


nums = [1,2,5,10,7,2,20,15,4]

mysort = Selection_sort()
mysort(nums)
print(nums)