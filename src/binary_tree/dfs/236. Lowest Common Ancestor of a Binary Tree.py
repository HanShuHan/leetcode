# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if node == p or node == q:
                return node

            left = right = None

            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            if left and not right:
                return left
            if right and not left:
                return right
            if left and right:
                return node

        return dfs(root)
