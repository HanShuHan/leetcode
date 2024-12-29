# Definition for src binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.p = None
        self.q = None

    def lowestCommonAncestor(self, root, p, q):
        self.p = p
        self.q = q

        def dfs(node):
            if node.val == self.p.val or node.val == self.q.val:
                return node

            left = right = None

            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right

        return dfs(root)
