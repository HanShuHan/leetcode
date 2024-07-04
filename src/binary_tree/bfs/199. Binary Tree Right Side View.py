# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            inner_queue = deque()
            while queue:
                cur = queue.popleft()
                if cur.left is not None:
                    inner_queue.append(cur.left)
                if cur.right is not None:
                    inner_queue.append(cur.right)
            result.append(cur.val)
            queue = inner_queue

        return result