class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Iterate from 0-n+1
        # Iterate through coins and subtract from i. If diff == 0 add to dict with 1. If diff in dict save as temp, continue iterating through nums
        # and find lowest temp option, add to dict. temp = -1. return dict[n]
        if amount == 0:
            return 0

        denoms = {}

        for i in range(amount+1):
            temp = -1
            for coin in coins:
                if i - coin == 0:
                    denoms[i] = 1
                    temp = -1
                    break
                if i - coin in denoms and (temp == -1 or denoms[i-coin] < temp): 
                    temp = denoms[i-coin]
            if temp != -1:
                denoms[i] = temp + 1

        return denoms[amount] if amount in denoms else -1
                