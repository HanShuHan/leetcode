import sys


class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first = second = sys.maxsize
        for num in nums:
            if num < first:
                first = num
            elif first < num < second:
                second = num
            elif second < num:
                return True

        return False
