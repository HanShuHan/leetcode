# Definition for src binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.count = 0

    def goodNodes(self, root):
        def dfs(node, curr_max):
            if node.val >= curr_max:
                self.count += 1

            if node.val > curr_max:
                curr_max = node.val

            if node.left:
                dfs(node.left, curr_max)
            if node.right:
                dfs(node.right, curr_max)

        dfs(root, root.val)

        return self.count
