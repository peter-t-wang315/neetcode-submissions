class StockSpanner:

    def __init__(self):
        self.spanStack = []

    def next(self, price: int) -> int:
        if len(self.spanStack) == 0:
            self.spanStack.append((price, 1))
            return 1

        latestPrice, span = self.spanStack[-1]

        if latestPrice > price:
            self.spanStack.append((price, 1))
            return 1
        
        newSpan = 1
        while latestPrice <= price:
            self.spanStack.pop()
            newSpan += span
            if len(self.spanStack) == 0:
                break
            tempPrice, tempSpan = self.spanStack[-1]
            latestPrice = tempPrice
            span = tempSpan
        self.spanStack.append((price, newSpan))

        return newSpan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)