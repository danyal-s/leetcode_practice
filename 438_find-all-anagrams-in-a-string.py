# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        
        for c in p:
            p_dict[c] = p_dict[c] + 1 if c in p_dict else 1
        
        count = len(p)
        i, j = 0, 0
        res = []
        
        while j < len(s):
            if s[j] in p_dict:
                p_dict[s[j]] -= 1
                count -= 1
            
            if count == 0 and all(x == 0 for x in p_dict.values()):
                res.append(i)
            
            if j - i + 1 == len(p):
                if s[i] in p_dict:
                    p_dict[s[i]] += 1
                    count += 1
                i += 1
            
            j += 1

        return res
