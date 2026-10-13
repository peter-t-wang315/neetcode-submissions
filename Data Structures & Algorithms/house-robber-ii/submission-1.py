class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            max1, max2 = 0, 0

            for num in nums:
                temp = max(max1+num, max2)
                max1 = max2
                max2 = temp
            
            return max(max1, max2)
        
        return max(helper(nums[1:]), helper(nums[:-1]))
