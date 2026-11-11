class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0
        # index iterate from left to right
        # while we have some sort of palindrome, continue to check for even/odd palindromes
        # if we hit the end of our string, break out
        for i in range(len(s)):
            left_i = i
            right_i = i
            even_palindrome = True
            odd_palindrome = True
            while right_i < len(s) and left_i >= 0 and ((odd_palindrome and s[right_i] == s[left_i]) or (right_i + 1 < len(s) and even_palindrome and s[right_i + 1] == s[left_i])):
                if odd_palindrome and s[right_i] == s[left_i]:
                    palindrome_count += 1
                else:
                    odd_palindrome = False
                if right_i + 1 < len(s) and even_palindrome and s[right_i + 1] == s[left_i]:
                    palindrome_count += 1
                else:
                    even_palindrome = False
                
                right_i += 1
                left_i -= 1
        
        return palindrome_count
