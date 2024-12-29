from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        # initially all rotten, gradually rotten in steps, never will

        m = len(grid)
        n = len(grid[0])
        rotten_oranges = deque()
        good = 0
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        round = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    good += 1

        if good == 0:
            return 0

        while rotten_oranges:
            round += 1

            for i in range(len(rotten_oranges)):
                row, col = rotten_oranges.popleft()

                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc

                    if (0 <= new_row < m and 0 <= new_col < n
                            and grid[new_row][new_col] == 1):
                        rotten_oranges.append((new_row, new_col))
                        good -= 1
                        grid[new_row][new_col] = 2

            if good == 0:
                return round

        return -1