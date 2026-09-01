class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            try:
                numStack.append(int(token))
            except:
                num1 = numStack.pop()
                num2 = numStack.pop()
                res = 0
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num1 * num2
                elif token == "/":
                    res = num2 / num1

                numStack.append(int(res))
        
        return numStack[0]