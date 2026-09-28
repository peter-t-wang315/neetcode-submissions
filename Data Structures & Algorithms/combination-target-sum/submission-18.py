class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(i, curr_sum, path):
            if curr_sum == target:
                ret.append(path.copy())
                return

            if i >= len(nums) or curr_sum > target:
                return

            dfs(i, curr_sum + nums[i], path + [nums[i]])
            dfs(i+1, curr_sum, path)

        
        dfs(0, 0, [])

        return ret
            
