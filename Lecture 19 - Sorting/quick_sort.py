class QuickSort:

    def quick_sort(self, start, end, arr):
        if start >= end:
            return
        mid = self.helper(start, end, arr)
        self.quick_sort(start, mid - 1, arr)
        self.quick_sort(mid + 1, end, arr)

    def helper(self, start, end, nums):
        pivot = nums[start]
        p1 = start + 1
        p2 = end

        while p1 <= p2:
            if nums[p1] <= pivot:
                p1 += 1
            elif nums[p2] > pivot:
                p2 -= 1
            else:
                nums[p1] , nums[p2] = nums[p2], nums[p1]

            
        nums[start], nums[p2] = nums[p2], nums[start]
        return p2


mysort = QuickSort()
nums = [21,1,5,80,61,20]
mysort.quick_sort(0, len(nums) - 1, nums)
print(nums)
