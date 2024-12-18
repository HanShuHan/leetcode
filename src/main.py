from collections import Counter, defaultdict


class Solution(object):
    def longestZigZag(self, root):
        count = 0
        max_path_len = 0
        direction = ''

        def dfs(node):
            if not node:
                return

            nonlocal count
            print(count)
            nonlocal max_path_len
            nonlocal direction

        dfs(root)


if __name__ == '__main__':
    new_row, new_col = 1 + 1, 2 + 2
    print(new_row)
    print(new_col)
