class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # helper function takes index, path
        # if our len(path) == k: return path.copy
        # else iterate deeper
        # iterating deeper needs to loop through all points from index+1 and down

        ret = []
        def helper(i, path):
            if len(path) == k:
                ret.append(path.copy())
                return
            
            for j in range(i, n+1):
                helper(j+1, [*path, j])
            
        helper(1, [])

        return ret