# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        io_l_end = inorder.index(preorder[0])

        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1:io_l_end+1], inorder[:io_l_end])
        node.right = self.buildTree(preorder[io_l_end+1:], inorder[io_l_end+1:])

        return node
    