# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + int((r - l + 1) / 2)
            
            if nums[mid] == target:
                return mid
            
            
            if nums[mid] > nums[r]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
