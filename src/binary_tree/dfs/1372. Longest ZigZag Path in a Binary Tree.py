# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.max_path = 0

    def longestZigZag(self, root):
        if not root.left and not root.right:
            return 0

        def dfs(node, count, direction):
            self.max_path = max(count, self.max_path)

            if node.left:
                dfs(node.left, 1 if direction == 'L' else count + 1, 'L')
            if node.right:
                dfs(node.right, 1 if direction == 'R' else count + 1, 'R')

        if root.left:
            dfs(root.left, 1, 'L')
        if root.right:
            dfs(root.right, 1, 'R')

        return self.max_path
