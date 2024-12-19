class Solution(object):
    def findPeakElement(self, nums):
        size = len(nums)
        if size == 1:
            return 0

        left, right = 0, size - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
