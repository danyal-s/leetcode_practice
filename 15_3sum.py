# https://leetcode.com/problems/3sum/
class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets = [nums[i], nums[j], nums[k]]
                        triplets.sort()
                        res.add(tuple(triplets))
        
        return res
                    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        for l in range(0, len(nums) - 2):
            r = len(nums) - 1
            mid = l + 1
            while mid < r:
                triplets = (nums[l], nums[mid], nums[r])
                triplets_sum = sum(triplets)

                if triplets_sum == 0:
                    res.add(triplets)
                
                if triplets_sum <= 0:
                    mid += 1
                
                elif triplets_sum > 0:
                    r -= 1

        return res
