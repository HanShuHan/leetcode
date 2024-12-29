from collections import deque


class Solution(object):
    def longestOnes(self, nums, k):
        queue = deque([])
        zeros = 0
        max_len = 0

        for num in nums:
            queue.append(num)

            if num == 0:
                zeros += 1

            while zeros > k:
                left = queue.popleft()
                if left == 0:
                    zeros -= 1

            curr_size = len(queue)
            if curr_size > max_len:
                max_len = curr_size

        return max_len
