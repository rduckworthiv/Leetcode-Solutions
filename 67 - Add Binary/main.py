class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert str to int, add, return binary string
        # note: add slice [2:] to cut out "0b"
        return bin(int(a, 2) + int(b, 2))[2:]