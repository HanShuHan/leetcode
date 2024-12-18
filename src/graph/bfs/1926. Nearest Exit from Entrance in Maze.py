from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        m = len(maze)
        n = len(maze[0])

        if m == n == 1:
            return -1

        visited = set()
        visited.add((entrance[0], entrance[1]))
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])

        while queue:
            row, col, steps = queue.popleft()

            if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and steps > 0:
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < m and 0 <= new_col < n
                        and maze[new_row][new_col] == '.'
                        and (new_row, new_col) not in visited):
                    queue.append([new_row, new_col, steps + 1])
                    visited.add((new_row, new_col))

        return -1
