class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapOfKLargestAsc = nums[:k]

        heapq.heapify(heapOfKLargestAsc)
        for i in range(k, len(nums)):
            if heapOfKLargestAsc[0] < nums[i]:
                heapq.heappop(heapOfKLargestAsc)
                heapq.heappush(heapOfKLargestAsc, nums[i])

        return heapOfKLargestAsc[0]