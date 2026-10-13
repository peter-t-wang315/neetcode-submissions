class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        def helper(path, i):
            if i == len(nums):
                ret.append(path)
                return
            
            helper([*path, nums[i]], i+1)

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            helper([*path], i+1)
                
        helper([], 0)
        return ret