# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return []
        
        digit_to_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def search(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            chars = digit_to_letter_map[digits[i]]

            for c in chars:
                search(i+1, cur_str + c)
        
        search(0, "")
        
        return res
