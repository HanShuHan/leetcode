# Definition for src binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        def dfs(node, curr_depth):
            curr_depth += 1
            if curr_depth > self.max_depth:
                self.max_depth = curr_depth

            if node.left:
                dfs(node.left, curr_depth)
            if node.right:
                dfs(node.right, curr_depth)

        dfs(root, 0)

        return self.max_depth
