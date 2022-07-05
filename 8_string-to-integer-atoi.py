# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def oldmyAtoi(self, s: str) -> int:
        res = 0
        i = 0
        sign = 1
        
        if not s or len(s) == 0:
            return res
        
        # skip whitespsace
        while s[i] == " ":
            i+=1
            if i == len(s):
                return res

        # find sign
        if s[i] == "-":
            sign = -1
        
        if s[i] in ("+", "-"):
            i+=1


        valid_digits = ('0','1','2','3','4','5','6','7','8','9')
        
        while i < len(s) and s[i] in valid_digits:
            res *= 10
            res += sign * int(s[i])
            
            if sign == 1 and res > (2**31) - 1:
                return (2**31) - 1
            elif sign == -1 and res < -2**31:
                return -(2**31)

            i += 1
        
        return res
