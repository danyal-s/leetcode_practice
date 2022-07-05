# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26
        
        for c in s:
            chars[ord(c) - ord("a")] += 1
        
        for c in t:
            chars[ord(c) - ord("a")] -= 1
            
        return all(c == 0 for c in chars)
