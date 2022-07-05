# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def _combinationSum(start, target, chosen):
            for i in range(start, len(candidates)):
                if target - candidates[i] < 0:
                    continue
                
                elif target - candidates[i] > 0:
                    chosen.append(candidates[i])
                    _combinationSum(i, target-candidates[i], chosen)
    
                else:
                    chosen.append(candidates[i])
                    res.append(tuple(chosen))
                
                chosen.pop()

        _combinationSum(0, target, [])
        return res
