# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def helper(curr):
            nonlocal prev
            if curr == None:
                return True
            
            if not helper(curr.left):
                return False
            if prev >= curr.val:
                return False
            prev = curr.val
            if not helper(curr.right):
                return False
            return True
        
        return helper(root)
            
        