class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # iterate to n-2 in list
        # cost[i+2] = cost[i+2] + Min(cost[i], cost[i+1])

        for i in range(len(cost)-2):
            cost[i+2] = cost[i+2] + min(cost[i], cost[i+1])
        
        return min(cost[len(cost)-1], cost[len(cost)-2])