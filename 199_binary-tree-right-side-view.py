# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        # Represents next level
        q_next_level = deque([root])

        res = []

        while len(q_next_level) > 0:
            q_current_level, q_next_level = q_next_level, deque()
            while len(q_current_level) > 0:

                cur_node = q_current_level.popleft()
                
                if cur_node.left:
                    q_next_level.append(cur_node.left)

                if cur_node.right:
                    q_next_level.append(cur_node.right)
            
            res.append(cur_node.val)
            
        return res
       
