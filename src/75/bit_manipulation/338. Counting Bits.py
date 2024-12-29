class Solution(object):
    def countBits(self, n):
        # 0, 1, 2, 3, 4, 5, 6, 7
        # [0]: 000 -> 0
        # [1]: 001 -> 1
        # [2]: 010 -> 1
        # [3]: 011 -> 2
        # [4]: 100 -> 1
        # [5]: 101 -> 2
        # [6]: 110 -> 2
        # [7]: 111 -> 3

        if n == 0:
            return [0]

        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
