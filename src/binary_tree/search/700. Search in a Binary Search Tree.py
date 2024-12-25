# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if root.val == val:
            return root
        elif val > root.val and root.right:
            return self.searchBST(root.right, val)
        elif val < root.val and root.left:
            return self.searchBST(root.left, val)

        return None
