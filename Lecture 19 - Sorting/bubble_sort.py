class bubbleSort():

    def __init__(self):
        pass

    def __call__(self, nums):
        n = len(nums)
        for j in range(n):
            for i in range(1,n-j):
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]


nums = [1,2,5,10,7,2,20,15,4]

mysort = bubbleSort()
mysort(nums)
print(nums)
