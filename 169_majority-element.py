# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_element = None
        count = 1
        for num in nums:
            if num != maj_element:
                count -= 1
                if count == 0:
                    maj_element = num
                    count = 1
            else:
                count += 1
        
        return maj_element
