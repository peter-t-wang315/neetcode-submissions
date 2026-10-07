class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Iterate through nums with i, if i-1 and i-2 in nums, find max of the two and add them to nums[i] continue to move
        for i in range(len(nums)):
            if i-3 >= 0:
                nums[i] = max(nums[i-2],nums[i-3]) + nums[i]
            elif i-2 >= 0:
                nums[i] = nums[i] + nums[i-2]
        
        print(nums)
        return max(nums[len(nums)-1], nums[len(nums)-2])
