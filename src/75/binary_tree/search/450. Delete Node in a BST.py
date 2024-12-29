# Definition for src binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_min_val(self, node):
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root, key):
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # root.val == key
            if root.left and root.right:
                right_min_val = self.find_min_val(root.right)
                root.val = right_min_val

                new_right = self.deleteNode(root.right, right_min_val)
                root.right = new_right
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None

        return root
