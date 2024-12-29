import heapq


class Solution(object):
    def totalCost(self, costs, k, candidates):
        costs_len = len(costs)

        if costs_len == 1:
            return costs[0]

        heap1 = []
        heap2 = []
        left, right = 0, costs_len - 1
        total = 0

        for i in range(candidates):
            if left <= right:
                heapq.heappush(heap1, costs[left])
                left += 1

            if left <= right:
                heapq.heappush(heap2, costs[right])
                right -= 1

        for _ in range(k):
            min_cost = 0

            if (heap1 and not heap2
                    or heap1 and heap2 and heap1[0] <= heap2[0]):
                min_cost = heapq.heappop(heap1)

                if left <= right:
                    heapq.heappush(heap1, costs[left])
                    left += 1
            else:
                min_cost = heapq.heappop(heap2)

                if left <= right:
                    heapq.heappush(heap2, costs[right])
                    right -= 1

            total += min_cost

        return total