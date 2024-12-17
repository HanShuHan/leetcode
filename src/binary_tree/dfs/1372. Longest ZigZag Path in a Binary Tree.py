# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_len = 0

    def dfs(self, node, direction, accum_len):
        if not node:
            return

        self.max_len = max(accum_len, self.max_len)

        if node.left:
            self.dfs(node.left, 'L', accum_len + 1 if direction == 'R' else 1)
        if node.right:
            self.dfs(node.right, 'R', accum_len + 1 if direction == 'L' else 1)

    def longestZigZag(self, root):
        if not root.left and not root.right:
            return 0

        if root.left:
            self.dfs(root.left, 'L', 1)
        if root.right:
            self.dfs(root.right, 'R', 1)

        return self.max_len
