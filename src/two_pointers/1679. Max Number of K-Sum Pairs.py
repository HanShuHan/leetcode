class Solution(object):
    def maxOperations(self, nums, k):
        size = len(nums)

        if size == 1:
            return 0

        count = 0
        left, right = 0, size - 1
        average = k // 2

        nums.sort()

        while left < right and nums[left] <= average:
            curr_sum = nums[left] + nums[right]

            if curr_sum > k:
                right -= 1
            elif curr_sum == k:
                count += 1
                left, right = left + 1, right - 1
            else:
                left += 1

        return count
