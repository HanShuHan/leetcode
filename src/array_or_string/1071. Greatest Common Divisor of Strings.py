import math


class Solution(object):
    def gcd(self, a, b):
        if b > a:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a

    def gcdOfStrings(self, str1, str2):
        s1_len, s2_len = len(str1), len(str2)
        gcd_len = self.gcd(s1_len, s2_len)

        div = str1[:gcd_len]

        div_divides_str1 = div * (s1_len // gcd_len) == str1
        div_divides_str2 = div * (s2_len // gcd_len) == str2

        if div_divides_str1 and div_divides_str2:
            return div
        else:
            return ''
