class Solution(object):
    def minFlips(self, a, b, c):
        # src = 4, b = 2, c = 7
        # 0100
        # 0010
        # ----
        # 0111

        flips = 0

        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                if bit_a == 1:
                    flips += 1
                if bit_b == 1:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
