# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        recorded_sum = {0: 1}

        def dfs(node, accum_sum):
            if not node:
                return 0

            accum_sum += node.val
            count = recorded_sum.get(accum_sum - targetSum, 0)
            recorded_sum[accum_sum] = recorded_sum.get(accum_sum, 0) + 1

            count += dfs(node.left, accum_sum)
            count += dfs(node.right, accum_sum)

            recorded_sum[accum_sum] = recorded_sum.get(accum_sum) - 1

            return count

        return dfs(root, 0)
