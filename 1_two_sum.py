# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """O(n^2) with O(1) space"""
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        
    def twoSumFaster(self, nums: List[int], target: int) -> List[int]:
        """O(nlogn) with O(n) space"""
        
        i, j = 0, len(nums) - 1
        
        nums2 = [(x, i) for i, x in enumerate(nums)]
        nums2.sort(key=lambda x: x[0])
        
        ij_sum = nums2[i][0] + nums2[j][0]
        while ij_sum != target:
            
            if ij_sum > target:
                j-=1
            else:
                i+=1
                
            ij_sum = nums2[i][0] + nums2[j][0]
        
        return nums2[i][1], nums2[j][1]

        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(n) w/ O(n) space - most optimal and simplest logic
        """
        # Visited values as dict keys with their indexes as dict values
        visited_values = {}
        for i, x in enumerate(nums):
            if (target - x) in visited_values.keys():
                return i, visited_values[target - x]
            else:
                visited_values[x] = i
