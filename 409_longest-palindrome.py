https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_map = {}
        res = 0
        for c in s:
            if c not in letter_map:
                letter_map[c] = 0
            
            letter_map[c] += 1
            if letter_map[c] % 2 == 0:
                res += 2
        
        if any(l % 2 == 1 for l in letter_map.values()):
            res += 1
        
        return res
