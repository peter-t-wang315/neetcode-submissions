class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = currMin = 1

        for num in nums:
            t = num * currMax
            currMax = max(t, num * currMin, num)
            currMin = min(t, num * currMin, num)
            res = max(res, currMax)

        return res