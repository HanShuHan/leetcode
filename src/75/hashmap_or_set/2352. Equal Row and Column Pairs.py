from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)

        if n == 1:
            return 1

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        count = 0

        for i in range(n):
            s1 = []
            for j in range(n):
                s1.append(grid[i][j])
            d1[str(s1)] += 1

        for j in range(n):
            s2 = []
            for i in range(n):
                s2.append(grid[i][j])
            d2[str(s2)] += 1

        for key in d2.keys():
            if key in d1:
                count += d2[key] * d1[key]

        return count