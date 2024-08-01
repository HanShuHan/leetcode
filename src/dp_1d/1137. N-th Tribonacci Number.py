class Solution:
    def tribonacci(self, n: int) -> int:
        first3 = (0, 1, 1)

        if 0 <= n <= 2:
            return first3[n]

        n0, n1, n2 = first3
        for _ in range(n - 2):
            n0, n1, n2 = n1, n2, (n0 + n1 + n2)
        return n2


class Solution2:

    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1

        mapping = {
            0: 0,
            1: 1,
            2: 1
        }

        def tribonacciNth(n: int) -> int:
            if n in mapping:
                return mapping[n]
            else:
                result = tribonacciNth(n - 3) + tribonacciNth(n - 2) + tribonacciNth(n - 1)
                mapping[n] = result
                return result

        return tribonacciNth(n)
