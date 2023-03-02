class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strs are different lengths, no anagram
        if len(s) != len(t):
            return False 
        
        # hash maps to hold letter counts
        letters_of_s, letters_of_t = {}, {}

        # compute character by character
        for i in range(len(s)):
            # get value from dict hash map, val = 0 if not in dict hash map
            letters_of_s[s[i]] = 1 + letters_of_s.get(s[i], 0)
            letters_of_t[t[i]] = 1 + letters_of_t.get(t[i], 0)

        if letters_of_s == letters_of_t:
            return True
        else:
            return False