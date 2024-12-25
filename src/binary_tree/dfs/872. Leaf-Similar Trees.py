# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        leaf1, leaf2 = [], []

        def dfs(node, leaf):
            if not node.left and not node.right:
                leaf.append(node.val)
                return

            if node.left:
                dfs(node.left, leaf)
            if node.right:
                dfs(node.right, leaf)

        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
