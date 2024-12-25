class Solution:
    def findMaxAverage(self, nums, k):
        nums_len = len(nums)

        if nums_len == 1:
            return nums[0]

        total = max_total = 0

        for i in range(k):
            total += nums[i]
        max_total = total

        for j in range(k, nums_len):
            total += nums[j] - nums[j - k]
            if total > max_total:
                max_total = total

        return max_total * 1.0 / k
