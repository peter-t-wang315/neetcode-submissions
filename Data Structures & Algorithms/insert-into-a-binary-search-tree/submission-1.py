# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        curr = root

        while (curr != None and curr.val != val):
            if (curr.val > val):
                if (curr.left == None):
                    curr.left = TreeNode(val)
                curr = curr.left
            else:
                if (curr.right == None):
                    curr.right = TreeNode(val)
                curr = curr.right
            
    
        return root
                
