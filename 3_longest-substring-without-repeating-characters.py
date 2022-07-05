# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return None
        
        l_map = {}
        i, j = 0, 0
        res_len = 0
        
        while j < len(s):
            if s[j] not in l_map.keys():
                l_map[s[j]] = 0

            l_map[s[j]] += 1
            
            if l_map[s[j]] == 1:
                res_len = max(res_len, j - i + 1)

            elif l_map[s[j]] > 1:
                while l_map[s[j]] > 1:
                    l_map[s[i]] -= 1
                    i += 1
            
            j += 1
        
        return res_len
