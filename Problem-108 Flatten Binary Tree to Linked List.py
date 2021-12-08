# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Logic: Recurse on the node. If the node has a left child, then 
# we need to put that before its right child. For leaf node we 
# just return the node.

# Time Complexity: O(n)
# Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _helper(self, node):
        if not node:
            return
        
        if not node.left and not node.right:
            return node
        
        l = self._helper(node.left)
        r = self._helper(node.right)
        
        if l:
            l.right = node.right
            node.right = node.left
            node.left = None
        
        return r if r else l
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._helper(root)