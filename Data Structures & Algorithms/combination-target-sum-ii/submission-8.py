class Solution:
    # [1,2,3] 5
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = set()
        candidates.sort()
        def dfs(index, curr_sum, path):
            if index == len(candidates) or curr_sum > target:
                return
            # check, is current sum greater than the target. If so return and fail
            # Is current sum equal to target, if so add to set
            if curr_sum == target:
                ret.add(tuple(sorted(path)))
                return
            j = index + 1
            while j < len(candidates):
                dfs(j, curr_sum+candidates[j], [*path, candidates[j]])
                prev2 = candidates[j]
                while j < len(candidates) and candidates[j] == prev2:
                    j += 1
        i = 0
        while i < len(candidates):
            dfs(i, candidates[i], [candidates[i]])
            prev = candidates[i]
            while i < len(candidates) and candidates[i] == prev:
                i += 1
        return [list(tup) for tup in ret]