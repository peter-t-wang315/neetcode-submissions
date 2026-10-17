class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        visit = [False] * n
        path = []

        def helper():
            if len(path) == n:
                ret.append(path.copy())
                return
            
            for i in range(n):
                if visit[i]:
                    continue
                
                if i and nums[i] == nums[i-1] and not visit[i-1                ]:
                    continue
                visit[i] = True
                path.append(nums[i])
                helper()
                visit[i] = False
                path.pop()
        
        nums.sort()
        helper()
        return ret