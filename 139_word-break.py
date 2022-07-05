# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True
        
        for i in reversed(range(len(s))):
            for w in wordDict:
                if i + len(w) <= len(s) and w == s[i:i + len(w)]:
                    dp[i] = dp[i + len(w)] or dp[i]

        return dp[0]
