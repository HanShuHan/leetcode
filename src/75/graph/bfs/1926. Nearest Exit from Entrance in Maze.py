from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])

        if m == n == 1:
            return -1

        init_row, init_col = entrance
        queue = deque([(init_row, init_col, 0)])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set([(init_row, init_col)])

        while queue:
            for i in range(len(queue)):
                row, col, count = queue.popleft()

                if ((row == 0 or row == m - 1
                     or col == 0 or col == n - 1)
                        and count > 0):
                    return count

                count += 1
                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc

                    if (0 <= new_row < m and 0 <= new_col < n
                            and maze[new_row][new_col] == '.'
                            and (new_row, new_col) not in visited):
                        queue.append((new_row, new_col, count))
                        visited.add((new_row, new_col))

        return -1
