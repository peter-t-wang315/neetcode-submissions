class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        curr_prod = 1

        for num in nums:
            curr_prod *= num
            prefix.append(curr_prod)

        curr_prod = 1
        for num in reversed(nums):
            curr_prod *= num
            suffix.append(curr_prod)
        
        suffix.reverse()
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(suffix[i+1] * prefix[i-1])

        return res