class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        possibleSteps = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        while possibleSteps:
            step = possibleSteps.popleft()

            for dr, dc in dirs:
                nr, nc = step[0] + dr, step[1] + dc

                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':  # check valid
                    if (nr == 0 or nr == rows - 1) or (nc == 0 or nc == cols - 1):  # on the edge
                        return step[2] + 1

                    possibleSteps.append((nr, nc, step[2] + 1))
                    maze[nr][nc] = '+'

        return -1