class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combos = {}

        # Iterate from 1-target
        # Inner iterate through nums
        # Track the number of combos we're at for newTarget by simply adding combos[newTarget] += #
        # if newTarget - num == 0: We have 1 new combination
        # if newTarget - num in combos: We can use that number of old combinations 
        # outside of second loop, if newTarget > 0 add it to combos

        for newTarget in range(1, target+1):
            combos[newTarget] = 0
            for num in nums:
                if newTarget - num == 0:
                    combos[newTarget] += 1
                if newTarget - num in combos:
                    combos[newTarget] += combos[newTarget - num]
                
        return combos[target]