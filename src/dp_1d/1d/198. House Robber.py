class Solution(object):
    def rob(self, nums):
        nums_len = len(nums)

        if nums_len == 1:
            return nums[0]

        # dp(0) = nums[0]
        # dp(1) = max(nums[0], nums[1])
        # dp(2) = max(dp(1), dp(0) + nums[2])
        # dp(3) = max(dp(2), dp(1) + nums[3])
        # 0, 1, 2, 3
        prev_2, prev_1 = nums[0], max(nums[0], nums[1])

        for i in range(2, nums_len):
            curr = max(prev_1, prev_2 + nums[i])
            prev_2, prev_1 = prev_1, curr

        return prev_1
