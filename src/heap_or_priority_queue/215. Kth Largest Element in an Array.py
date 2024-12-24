import heapq


class Solution(object):
    def findKthLargest_1(self, nums, k):
        if len(nums) == 1:
            return nums[0]

        largest = heapq.nlargest(k, nums)

        return largest[-1]

    def findKthLargest_2(self, nums, k):
        nums_len = len(nums)

        if nums_len == 1:
            return nums[0]

        if k <= nums_len // 2:
            largest = heapq.nlargest(k, nums)
            return largest[-1]
        else:
            smallest = heapq.nsmallest(nums_len - k + 1, nums)
            return smallest[-1]

    # def findKthLargest_3(self, nums, k):
    #     nums_len = len(nums)
    #
    #     if nums_len == 1:
    #         return nums[0]
    #
    #     heap = nums[:k]
    #     heapq.heapify(heap)
    #
    #     for i in range(k, nums_len):
    #         if heap[0] < nums[i]:
    #             heapq.heappushpop(heap, nums[i])
    #
    #     return heap[0]
