# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        res = 0
        
        for p in prices:
            min_price = min(p, min_price)
            res = max(res, p - min_price)
            
        return res
