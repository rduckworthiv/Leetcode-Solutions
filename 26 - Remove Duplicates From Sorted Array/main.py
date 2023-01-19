class Solution:        
    def removeDuplicates(self, nums: List[int]) -> int:
        currentNum = -101
        length = 0
        for i in range(len(nums)):
            if nums[i] != currentNum:
                currentNum = nums[i]
                nums[length] = currentNum
                length+=1
        return length