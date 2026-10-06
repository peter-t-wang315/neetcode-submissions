# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        # if left/right == None: return
        # if curr val > largest: count++, largest = val
        # iterate left
        # iterate right 
        def dfs(curr, largest):
            nonlocal count
            if curr == None:
                return
            
            if curr.val >= largest:
                count += 1
                largest = curr.val

            dfs(curr.left, largest)
            dfs(curr.right, largest)
        
        dfs(root, -101)
        return count