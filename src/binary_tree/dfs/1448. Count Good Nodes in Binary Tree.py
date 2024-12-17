# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self._good = 0

    def goodNodes(self, root):
        self.goodNode(root, root.val)
        return self._good

    def goodNode(self, node, max_val):
        if not node:
            return

        if node.val >= max_val:
            self._good += 1

        max_val = max(node.val, max_val)

        if node.left:
            self.goodNode(node.left, max_val)
        if node.right:
            self.goodNode(node.right, max_val)
