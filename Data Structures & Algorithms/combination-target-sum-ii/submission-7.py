class Solution:
    # [1,2,3] 5

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def dfs(index, curr_sum, path):
            if curr_sum == target:
                ret.append(path.copy())
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i] > target:
                    break
                
                dfs(i + 1, curr_sum + candidates[i], [*path, candidates[i]])


        dfs(0, 0, [])
        return ret