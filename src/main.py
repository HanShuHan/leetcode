class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) == (0, 0):
            return 0

        pathsCount = 0
        curPosOfPaths = deque([[0, 0]])

        while curPosOfPaths:
            pos = curPosOfPaths.popleft()

            if pos == [m - 1, n - 1]:
                pathsCount += 1
            if pos[0] < m:
                curPosOfPaths.append([pos[0] + 1, pos[1]])
            if pos[1] < n:
                curPosOfPaths.append([pos[0], pos[1] + 1])

        return pathsCount


if __name__ == '__main__':
    # Start from here
    dp = [[1] * 3 for _ in range(10)]
    print(dp)
