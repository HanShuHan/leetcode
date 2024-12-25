class Solution(object):
    def minCostClimbingStairs(self, cost):
        # [1, 100, 1, 1, 1, 100]
        # dp(0) = cost[0]
        # dp(1) = cost[1]
        # dp(2) = min(dp(0), dp(1)) + cost[2]
        # dp(3) = min(dp(1), dp(2)) + cost[3]

        cost_len = len(cost)

        if cost_len == 2:
            return min(cost[0], cost[1])

        prev_1, prev_2 = cost[1], cost[0]

        for i in range(2, cost_len):
            curr = min(prev_1, prev_2) + cost[i]
            prev_1, prev_2 = curr, prev_1

        return min(prev_1, prev_2)
