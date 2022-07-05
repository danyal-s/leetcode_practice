# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
    
        q1 = deque()
		
		# Initialize queue with root
        q1.appendleft(root)
        res = []
        
        while len(q1) != 0:
            res2 = []
            
			# Transfer q1 reference to q2 for this scope
            q2 = q1
            
			# Assign new queue to q1
            q1 = deque()
            while len(q2) != 0:
                cur_node = q2.pop()
                res2.append(cur_node.val)

                if cur_node.left is not None:
                    q1.appendleft(cur_node.left)

                if cur_node.right is not None:
                    q1.appendleft(cur_node.right)
        
            res.append(res2)
        
        return res
