# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, None, None)
    
        
    def _isValidBST(self, root, lowest, highest):
        if root is None:
            return True
        
        if lowest is not None and root.val <= lowest:
            return False
        
        if highest is not None and root.val >= highest:
            return False
        
        
        return self._isValidBST(root.left, lowest, root.val) and self._isValidBST(root.right, root.val, highest)
