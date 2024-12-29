import heapq


class Solution(object):
    def maxScore(self, nums1, nums2, k):
        nums_len = len(nums1)

        if nums_len == 1:
            return nums1[0] * nums2[0]

        new_nums = sorted([(n2, n1) for n1, n2 in zip(nums1, nums2)], reverse=True)
        heap_n1 = []
        sum_of_n1 = 0
        min_of_n2 = new_nums[k - 1][0]

        for i in range(k):
            n1 = new_nums[i][1]
            heapq.heappush(heap_n1, n1)
            sum_of_n1 += n1
        max_product = sum_of_n1 * min_of_n2

        for j in range(k, nums_len):
            new_n1 = new_nums[j][1]

            if new_n1 > heap_n1[0]:
                sum_of_n1 += (new_n1 - heap_n1[0])
                heapq.heappushpop(heap_n1, new_n1)
                min_of_n2 = new_nums[j][0]

                max_product = max(sum_of_n1 * min_of_n2, max_product)

        return max_product
