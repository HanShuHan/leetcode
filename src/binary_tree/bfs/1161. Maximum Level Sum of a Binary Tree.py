from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        max_sum, level = root.val, 1
        curr_level = 0

        while queue:
            queue_len = len(queue)
            curr_sum = 0
            curr_level += 1

            for i in range(queue_len):
                node = queue.popleft()

                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                level = curr_level

        return level
