# https://leetcode.com/problems/valid-palindrome/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(re.findall("[A-Za-z0-9]", s))
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
