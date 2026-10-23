class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}

        def dfs(i):
            if (i in dp):
                return dp[i]

            # iterate through wordDict
            for word in wordDict:
                if i + len(word) and s[i:i+len(word)] == word: 
                    if dfs(i+len(word)): 
                        return True

            # outside of loop
            dp[i] = False
            return False
        
        return dfs(0)