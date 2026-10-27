class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        i0 = 0
        i2 = len(nums) - 1

        # while index over nums
        while i <= i2:
            if nums[i] == 0:
                nums[i] = nums[i0]
                nums[i0] = 0
                i0 += 1
            elif nums[i] == 2:
                nums[i] = nums[i2]
                nums[i2] = 2
                i2 -= 1
                i -= 1
            i += 1
        
        return nums
        # if nums[i] == 0: swap nums[i] with nums[i0], increase i0, i--
        # if nums[i] == 2: swap nums[i] with nums[i2], deecrement i2, i--
        # just continue
        