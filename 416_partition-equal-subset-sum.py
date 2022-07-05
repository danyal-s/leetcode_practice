# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        nums_sum = int(nums_sum / 2)
        
        dp = [[False if i != 0 else True for i in range(nums_sum + 1)] for _ in range(len(nums) + 1)]
        
        for res_i in range(1, len(dp[0])):
            for nums_i in range(1, len(dp)):
                
                dp_case_1 = dp[nums_i - 1][res_i - nums[nums_i - 1]] if res_i - nums[nums_i - 1] >= 0 else False
                dp_case_2 = dp[nums_i - 1][res_i]
                
                dp[nums_i][res_i] = dp_case_1 or dp_case_2

        return dp[-1][-1]
