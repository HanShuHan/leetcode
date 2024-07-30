class Solution:
    def tribonacci(self, n: int) -> int:
        first3 = (0, 1, 1)

        if 0 <= n <= 2:
            return first3[n]

        n0, n1, n2 = first3
        for _ in range(n - 2):
            n0, n1, n2 = n1, n2, (n0 + n1 + n2)
        return n2