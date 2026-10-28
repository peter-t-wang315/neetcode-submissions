import math

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum / 2

        # recurse down nums
        # if we reach the end of nums or our current list size is greater than half return False

        # for j in range(i, len(nums)):
        # if curr_sum + nums[i] == target: return True
        # if curr_sum + nums[i] < target: helper(curr_sum + nums[j], j)
        # if recursive call returns True, exit immediately and return True. If returns false just keep iterating and at the end return False
        def helper(i, curr_sum, subset_size):
            if (subset_size == math.ceil(len(nums) / 2)):
                return False
            
            for j in range(i, len(nums)):
                if curr_sum + nums[j] == target:
                    return True
                if curr_sum + nums[j] < target:
                    if helper(j+1, curr_sum + nums[j], subset_size + 1):
                        return True
                
            return False

        return helper(0, 0, 0)