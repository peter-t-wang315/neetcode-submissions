# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightSideViewHelper(root, 0, [])

    def rightSideViewHelper(self, curr, height, nodeVals): 
        if curr == None:
            return nodeVals
        if height == len(nodeVals):
            nodeVals.append(curr.val)

        if curr.right != None:
            nodeVals = self.rightSideViewHelper(curr.right, height+1, nodeVals)
        if curr.left != None:
            nodeVals = self.rightSideViewHelper(curr.left, height+1, nodeVals)

        return nodeVals
        
