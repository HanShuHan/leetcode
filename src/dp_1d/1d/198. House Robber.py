class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        prev1 = prev2 = 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, num + prev2)

        return prev1
