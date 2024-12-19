import heapq


class Solution(object):
    def totalCost(self, costs, k, candidates):
        left_heap, right_heap = [], []
        left, right = 0, len(costs) - 1
        total = 0

        for i in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1
            if right >= left:
                heapq.heappush(right_heap, costs[right])
                right -= 1

        for _ in range(k):
            if left_heap and not right_heap or left_heap and right_heap and left_heap[0] <= right_heap[0]:
                total += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(right_heap)
                if right >= left:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total
