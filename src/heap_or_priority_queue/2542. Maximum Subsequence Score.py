import heapq


class Solution(object):
    def maxScore(self, nums1, nums2, k):
        sorted_nums_pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        curr_sum = 0

        for i in range(k):
            num1 = sorted_nums_pairs[i][1]
            heapq.heappush(heap, num1)
            curr_sum += num1
            max_val = curr_sum * sorted_nums_pairs[k - 1][0]

        for i in range(k, len(sorted_nums_pairs)):
            new_num1 = sorted_nums_pairs[i][1]

            if new_num1 > heap[0]:
                curr_sum -= heap[0]
                curr_sum += new_num1
                heapq.heapreplace(heap, new_num1)

            max_val = max(curr_sum * sorted_nums_pairs[i][0], max_val)

        return max_val
