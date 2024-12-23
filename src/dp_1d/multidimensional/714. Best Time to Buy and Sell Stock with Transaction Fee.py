class Solution(object):
    def maxProfit(self, prices, fee):
        rounds = len(prices)
        if rounds == 1:
            return 0

        cash = 0
        stock = -prices[0]

        for i in range(1, rounds):
            new_cash = max(cash, prices[i] + stock - fee)
            new_stock = max(stock, cash - prices[i])

            cash, stock = new_cash, new_stock

        return cash
