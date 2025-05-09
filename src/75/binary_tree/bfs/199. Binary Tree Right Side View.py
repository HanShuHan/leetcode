from collections import deque


# Definition for src binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == queue_len - 1:
                    result.append(node.val)

        return result
