# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        prv = 2
        nxt = 3
        
        for _ in range(3, n):
            prv, nxt = nxt, prv + nxt
                        
        return nxt
