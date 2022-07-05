# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def _permute(chosen):
            if len(chosen) == len(nums):
                res.append(tuple(chosen))
                return
                
            for num in nums:
                if num not in chosen:
                    chosen.append(num)
                    _permute(chosen)
                    chosen.pop()
            
            
        _permute([])
        return res
