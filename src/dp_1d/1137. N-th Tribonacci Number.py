class Solution:
    def tribonacci(self, n: int) -> int:
        top3 = (0, 1, 1)

        if n <= 2:
            return top3[n]

        (n0, n1, n2) = top3

        for _ in range(n - 2):
            (n0, n1, n2) = (n1, n2, (n0 + n1 + n2))

        return n2
