# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_counts = [0]*26
        rn_letters = len(ransomNote)
        
        for c in ransomNote:
            ransom_note_counts[ord(c) - ord("a")] += 1
        
        for c in magazine:
            if rn_letters == 0: # optimization
                return True

            rn_idx = ord(c) - ord("a")
            if ransom_note_counts[rn_idx] > 0:
                rn_letters -= 1
                
            ransom_note_counts[rn_idx] -= 1
        
        return rn_letters == 0
