class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        def can_finish(k):
            total = 0
            for pile in piles:
                total += (pile + k - 1) // k
            return total <= h

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    Solution().minEatingSpeed([3, 6, 7, 11], 8)
