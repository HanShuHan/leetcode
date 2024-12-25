class Solution(object):
    def tribonacci(self, n):
        # 0, 1, 1, 2, 4
        #          0, 1

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # n == 3
        curr, prev_1, prev_2 = 2, 1, 1

        for _ in range(n - 3):
            curr, prev_1, prev_2 = curr + prev_1 + prev_2, curr, prev_1

        return curr
