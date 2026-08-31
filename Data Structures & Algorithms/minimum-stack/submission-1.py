class MinStack:
    def __init__(self):
        self.stack = []
        self.smallestStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallestStack) == 0 or self.smallestStack[-1] >= val:
            self.smallestStack.append(val)

    def pop(self) -> None:
        temp = self.stack[-1]
        self.stack.pop()
        if self.smallestStack[-1] == temp:
            self.smallestStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallestStack[-1]
