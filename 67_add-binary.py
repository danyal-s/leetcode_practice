# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_digits(a, b, carry):
            if a == "1" and b == "1":
                res = "1" if carry else "0"
                carry = True
            elif a == "1" or b == "1":
                res = "0" if carry else "1"
            else:
                res = "1" if carry else "0"
                carry = False
            
            return res, carry
        

        res = []
        ai, bi = len(a) - 1, len(b) - 1
        carry = False
        while ai > -1 or bi > -1:
            res_part, carry = add_digits(a[ai] if ai >= 0 else "0", b[bi] if bi >= 0 else "0", carry)
            res.append(res_part)
            ai -= 1
            bi -= 1
        
        res.append("1" if carry else "")
        
        return "".join(reversed(res))
