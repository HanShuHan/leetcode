class Solution(object):
    def findPeakElement(self, nums):
        nums_len = len(nums)

        if nums_len == 1:
            return 0

        left, right = 0, nums_len - 1

        while left < right:
            mid = (left + right) // 2
            curr_mid = nums[mid]

            if curr_mid < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
