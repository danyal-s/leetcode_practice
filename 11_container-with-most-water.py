# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxAreaBruteForce(self, height: List[int]) -> int:
        res = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if j <= i:
                    continue
                
                res = max(res, min(h2, h1)*(j - i))
        
        return res
    
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[r] <= height[l]:
                r -= 1
            else:
                l += 1
        
        return res