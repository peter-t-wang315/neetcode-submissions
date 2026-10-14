class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeFinder(l, r):
            nonlocal strStart
            nonlocal strLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > strLen:
                    strStart = l
                    strLen = r - l + 1
                l -= 1
                r += 1

        strStart = 0
        strLen = 0

        for i in range(len(s)):
            # odd length palindrome
            palindromeFinder(i, i)
            palindromeFinder(i, i+1)

        return s[strStart: strStart+strLen]