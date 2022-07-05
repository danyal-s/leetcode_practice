# https://leetcode.com/problems/coin-change/
import sys
class Solution:
    def coinChangeRec(self, coins: List[int], amount: int) -> int:
        
        def custom_min(vals):
            valid_vals = [x for x in vals if x!=-1]
            if len(valid_vals) > 0:
                return min(valid_vals)
            else:
                return -1

        dp_sols = {}
        def dp(ci, amt):
            if (ci, amt) in dp_sols:
                return dp_sols[ci, amt]
            
            nonlocal coins
            nonlocal amount
            if amt == amount:
                return 0
            
            sp1 = dp(ci, amt + coins[ci]) if amt + coins[ci] <= amount else -1
            if sp1 != -1:
                sp1 += 1
            
            dp_sols[ci, amt] = custom_min([
                sp1,
                dp(ci+1, amt) if ci+1 < len(coins) else -1
            ])
            
            return dp_sols[ci, amt]
            
            
    
        return dp(0, 0)

    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for a in range(1,len(dp)):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        
        return dp[-1] if dp[-1] != sys.maxsize else -1
