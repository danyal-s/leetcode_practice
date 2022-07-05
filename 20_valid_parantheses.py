# https://leetcode.com/problems/valid-parentheses/

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in "([{":
                stack.append(c)
            
            if c in ")]}":
                if len(stack) == 0:
                    return False
                
                opening_bracket = stack.pop()

                if opening_bracket == "(":
                    expected_closing_bracket = ")"
                elif opening_bracket == "[":
                    expected_closing_bracket = "]"
                else:
                    expected_closing_bracket = "}"
                    
                if c != expected_closing_bracket:
                    return False

        return True if len(stack) == 0 else False
