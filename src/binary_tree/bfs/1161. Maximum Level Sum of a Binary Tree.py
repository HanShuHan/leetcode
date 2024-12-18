from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        if not root.left and not root.right:
            return 1

        curr_level = 0
        level = 1
        queue = deque([root])
        max_sum = root.val

        while queue:
            row_sum = 0
            curr_level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                row_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if row_sum > max_sum:
                max_sum = row_sum
                level = curr_level

        return level
