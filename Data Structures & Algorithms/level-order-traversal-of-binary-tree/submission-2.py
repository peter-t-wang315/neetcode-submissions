# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Declare your external vars to store level values
        res = []

        def treeTraversal(curr, height):
            if curr == None:
                return
            # Take curr val and add it to list[height]
            if height == len(res):
                res.append([])
            res[height].append(curr.val)
            # Traverse left incrementing its height
            treeTraversal(curr.left, height+1)
            # Traverse right incrementing its height
            treeTraversal(curr.right, height+1)
        
        treeTraversal(root, 0)
        return res