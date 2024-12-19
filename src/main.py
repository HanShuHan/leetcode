import heapq
from bisect import bisect_left
from collections import Counter, defaultdict


class Solution(object):
    def longestZigZag(self, root):
        count = 0
        max_path_len = 0
        direction = ''

        def dfs(node):
            if not node:
                return

            nonlocal count
            print(count)
            nonlocal max_path_len
            nonlocal direction

        dfs(root)


if __name__ == '__main__':
    from bisect import bisect_left

    # Sorted list
    a = [1, 3, 4, 7, 9]

    # Find the index to insert 4
    index = bisect_left(a, 99)
    print(index)  # Output: 2 (index of the first 4)

    # Find the index to insert 5
    index = bisect_left(a, 5)
    print(index)  # Output: 3 (would insert before 7)

    # Custom range
    index = bisect_left(a, 4, lo=1, hi=3)
    print(index)  # Output: 2 (within the range 1 to 3)

