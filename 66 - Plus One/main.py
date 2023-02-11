class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)-1, -1, -1):
            num += (digits[i]*10**(len(digits)-1 - i))
        num += 1
        return [int(x) for x in str(num)]