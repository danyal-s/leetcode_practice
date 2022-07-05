# https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque
class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
            
        self.s2.append(x)
        
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

    def pop(self) -> int:
        return self.s2.pop()
        

    def peek(self) -> int:
        res = self.s2.pop()
        self.s2.append(res)
        return res
        

    def empty(self) -> bool:
        return len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
