class Solution:
    def climbStairs(self, n: int) -> int:
        stair_combos = [1,2]

        for i in range(n-2):
            stair_combos.append(stair_combos[i]+ stair_combos[i+1])

        return stair_combos[n-1]