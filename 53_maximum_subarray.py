# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArrayNTime(self, nums: List[int]) -> int:
        cur = -10001
        max_res = -10001
        for num in nums:
            cur = max(num, num + cur)
            max_res = max(cur, max_res)
        return max_res
            
    
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums
            
        l = self.maxSubArray(nums[:len(nums)//2])
        r = self.maxSubArray(nums[len(nums)//2:])
        
        return max(r, l+r)
            
