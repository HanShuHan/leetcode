from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        rotten_oranges = deque()
        good_oranges = 0
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        for i in range(m):
            for j in range(n):
                g = grid[i][j]

                if g == 2:
                    rotten_oranges.append((i, j))
                    visited.add((i, j))
                elif g == 1:
                    good_oranges += 1

        if good_oranges == 0:
            return 0

        while rotten_oranges:
            for i in range(len(rotten_oranges)):
                rotten_orange = rotten_oranges.popleft()

                for dr, dc in directions:
                    new_row, new_col = rotten_orange[0] + dr, rotten_orange[1] + dc

                    if (0 <= new_row < m and 0 <= new_col < n
                            and (new_row, new_col) not in visited
                            and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        good_oranges -= 1
                        rotten_oranges.append((new_row, new_col))

            minutes += 1
        minutes -= 1

        if good_oranges > 0:
            return -1
        return minutes
