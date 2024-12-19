import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if heap[0] < num:
                heapq.heapreplace(heap, num)

        return heap[-k]
