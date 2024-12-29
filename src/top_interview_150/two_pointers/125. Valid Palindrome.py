class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric = ''

        for c in s:
            if c.isalnum():
                alpha_numeric += c.lower()

        left, right = 0, len(alpha_numeric) - 1

        while left < right:
            if alpha_numeric[left] != alpha_numeric[right]:
                return False
            left += 1
            right -= 1

        return True
