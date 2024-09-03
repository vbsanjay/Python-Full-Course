class MergeSort:
    def merge_sort(self, nums, start, end):

        if start == end:
            return
        
        mid = start + (end - start) // 2
        self.merge_sort(nums, start, mid)
        self.merge_sort(nums, mid + 1, end)
        self.merge_sorted_arrays(nums, start, mid, end)

    def merge_sorted_arrays(self, nums, start, mid, end):
        if len(nums) == 1:
            return nums
        
        temp = []

        p1 = start
        p2 = mid + 1

        while p1 <= mid and p2 <= end:
            if nums[p1] < nums[p2]:
                temp.append(nums[p1])
                p1 += 1
            else:
                temp.append(nums[p2])
                p2 += 1

        while p1 <= mid:
            temp.append(nums[p1])
            p1 += 1

        while p2 <= end:
            temp.append(nums[p2])
            p2 += 1

        for i in range(start, end +1):
            nums[i] = temp[i - start]

mysort = MergeSort()
nums = [21,1,5,80,61,20]
mysort.merge_sort(nums, 0, len(nums) - 1)
print(nums)