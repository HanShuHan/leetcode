from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):
        count = 0
        d = defaultdict(int)
        for row in grid:
            d[str(row)] += 1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            c = d[str(col)]
            if c > 0:
                count += c

        return count

    def equalPairs2(self, grid):
        count = 0
        grid_size = len(grid)
        row_size = len(grid[0])

        for row in grid:
            for i in range(row_size):
                equal = True
                for j in range(grid_size):
                    if row[j] != grid[j][i]:
                        equal = False
                if equal:
                    count += 1

        return count

    def equalPairs3(self, grid):
        count = 0
        row_size = len(grid[0])

        for row in grid:
            for i in range(row_size):
                if all(row[j] == grid[j][i] for j in range(row_size)):
                    count += 1

        return count


if __name__ == '__main__':
    _grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    Solution().equalPairs(_grid)
