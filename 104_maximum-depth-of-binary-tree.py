# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        res = 0
        
        def dfs(root):
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            nonlocal res
            res = max(res, l, r)

            return max(l, r) + 1

        dfs(root)
        return res + 1
