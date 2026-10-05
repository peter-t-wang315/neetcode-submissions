class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        # Base case: if len(path) == len(nums): append, return
        # for val in nums: if val in path_set: skip, else backtrack
        def backtrack(path, path_set):
            if len(path) == len(nums):
                ret.append(path)
                return
            
            for val in nums:
                if not val in path_set:
                    backtrack([*path, val], {*path_set, val})
        backtrack([], set())

        return ret