class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = {}
        for word in dictionary:
            curr = root
            for c in word: 
                curr = curr.setdefault(c, {})
            curr["."] = True

        n = len(s)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            node = root
            for j in range(i, n):
                if s[j] not in node:
                    break
                node = node[s[j]]
                if "." in node:
                    dp[i] = min(dp[i], dp[j+1])
        
        return dp[0]