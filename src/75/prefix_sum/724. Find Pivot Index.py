class Solution(object):
    def pivotIndex(self, nums):
        nums_len = len(nums)

        if nums_len == 1:
            return 0

        left, right = 0, sum(nums) - nums[0]

        if left == right:
            return 0

        for i in range(1, nums_len):
            right -= nums[i]
            left += nums[i - 1]

            if left == right:
                return i

        return -1
