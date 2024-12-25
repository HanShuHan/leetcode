class Solution(object):
    def maxProfit(self, prices, fee):
        rounds = len(prices)

        if rounds == 1:
            return 0

        cash = 0
        hold = -prices[0]

        for i in range(1, rounds):
            new_cash = max(cash, prices[i] + hold - fee)
            new_hold = max(hold, cash - prices[i])
            cash, hold = new_cash, new_hold

        return cash
