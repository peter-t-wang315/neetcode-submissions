class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
        # helper function takes numOpen, numClose
        def helper(numOpen, numClose):
            # base case: if numOpen == numClose == n: string join stack and push to output
            if numOpen == numClose == n: 
                output.append("".join(stack))
            # if numOpen < n: add "(" to stack, recurse down, pop stack
            if numOpen < n:
                stack.append("(")
                helper(numOpen+1, numClose)
                stack.pop()
            # if numClose < numOpen: add ")" to stack, recurse down, pop stack
            if numClose < numOpen:
                stack.append(")")
                helper(numOpen, numClose+1)
                stack.pop()

        helper(0,0)
        return output