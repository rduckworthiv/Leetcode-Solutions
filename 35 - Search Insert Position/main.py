class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # iterate through list
        # is num present in list?
            # y:
                # return index of num
            # n: find index of num smaller, return i+1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)