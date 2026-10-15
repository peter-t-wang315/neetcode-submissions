class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # iterate through s with i. Every i, palindrome check by keeping l/r = i or l = i and r = i+1. Every substring add to count
        # find palindrome:
        # if s[l] != s[r]: return
        # else iterate and add to count
        def palindrome_finder(l, r):
            nonlocal count

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return
                count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            palindrome_finder(i, i)
            palindrome_finder(i, i+1)
        
        return count