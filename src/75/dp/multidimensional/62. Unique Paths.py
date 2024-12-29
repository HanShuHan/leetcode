class Solution(object):
    def uniquePaths(self, m, n):
        if m == n == 1:
            return 1

        path = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[-1][-1]