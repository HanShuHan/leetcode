from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.targetSum = None
        self.count = 0
        self.path_sum = defaultdict(int)
        self.path_sum[0] = 1

    def pathSum(self, root, targetSum):
        if not root:
            return 0

        self.targetSum = targetSum

        def dfs(node, curr_sum):
            curr_sum += node.val
            self.count += self.path_sum[curr_sum - self.targetSum]
            self.path_sum[curr_sum] += 1

            if node.left:
                dfs(node.left, curr_sum)
            if node.right:
                dfs(node.right, curr_sum)

            self.path_sum[curr_sum] -= 1

        dfs(root, 0)

        return self.count
