class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        comboDict = {}
        i = 1
        # First, find all perfect squares up until n
        while i*i <= n:
            squares.append(i*i)
            i+=1

        for target in range(1, n+1):
        # iterate over all perfect squares
            for square in squares:
                # if target - perfect square == 0: add 1 to the combinations dict and continue
                if target - square == 0:
                    comboDict[target] = 1
                    break
                
                # if target - perfect square in comboDict: comboDict[target] = Min(comboDict[perfSquare] + comboDict[target - perfSquare], comboDict[target])
                elif target-square in comboDict:
                    comboDict[target] = min(comboDict[square] + comboDict[target - square], comboDict.get(target, math.inf))

        return comboDict[n]