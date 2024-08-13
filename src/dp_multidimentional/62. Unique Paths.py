class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        posPathsCount = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                posPathsCount[i][j] = posPathsCount[i][j - 1] + posPathsCount[i - 1][j]

        return posPathsCount[m - 1][n - 1]