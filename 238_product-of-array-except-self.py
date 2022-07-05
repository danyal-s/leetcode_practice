# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num
        
        suffix = 1
        for i in reversed(range(len(nums))):
            num = nums[i]
            res[i] = suffix * res[i]
            suffix *= num
        
        return res
