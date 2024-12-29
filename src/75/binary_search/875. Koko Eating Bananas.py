class Solution(object):
    def minEatingSpeed(self, piles, h):
        piles_len = len(piles)
        max_pile = max(piles)

        if piles_len == h:
            return max_pile

        left, right = 1, max_pile

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours > h:
                left = mid + 1
            else:
                right = mid

        return left
