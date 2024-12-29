from collections import deque


class Solution(object):
    def longestSubarray(self, nums):
        size = len(nums)

        if size == 1:
            return 0

        queue = deque([])
        zeros = 0
        max_len = 0

        for num in nums:
            queue.append(num)

            if num == 0:
                zeros += 1

            while zeros > 1:
                left = queue.popleft()
                if left == 0:
                    zeros -= 1

            curr_len = len(queue) - zeros
            if curr_len > max_len:
                max_len = curr_len

        if max_len == size:
            max_len -= 1

        return max_len
