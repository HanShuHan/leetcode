class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        comparables = []
        comparable = 0

        for i in range(k):
            comparable += nums[i]
        comparables.append(comparable)

        for i in range(k, len(nums)):
            comparable += nums[i]
            comparable -= nums[i - k]
            comparables.append(comparable)

        return max(comparables) / k
