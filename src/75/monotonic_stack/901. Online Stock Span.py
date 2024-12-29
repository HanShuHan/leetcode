class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and price >= self.stack[-1][0]:
            prev_price, prev_span = self.stack.pop()

            span += prev_span
        self.stack.append((price, span))

        return span
