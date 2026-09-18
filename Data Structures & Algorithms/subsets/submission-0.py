class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for inputNums in nums:
            for outputNums in output[:]:
                temp = outputNums[:]
                temp.append(inputNums)
                output.append(temp)
            output.append([inputNums])
        output.append([])
        return output