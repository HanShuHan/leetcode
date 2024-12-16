class Solution(object):
    def longestOnes(self, nums, k):
        zero_count = 0
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                left += 1
                if nums[left - 1] == 0:
                    zero_count -= 1

            max_length = max(max_length, right - left + 1)

        return max_length