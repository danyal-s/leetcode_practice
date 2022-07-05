# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        mid = ((r - l) // 2) + l
        
        while l < r:
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
            
            mid = ((r - l) // 2) + l

        return mid
