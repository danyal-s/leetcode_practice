# https://leetcode.com/problems/min-stack/


from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            min_val = self.min_stack.pop()
            self.min_stack.append(min_val)
            
            if val < min_val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        val = self.stack.pop()
        self.stack.append(val)
        return val
        

    def getMin(self) -> int:
        min_val = self.min_stack.pop()
        self.min_stack.append(min_val)
        return min_val
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
