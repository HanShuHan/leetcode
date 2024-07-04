# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        layerTrees = deque()
        layerTrees.append(root)

        while layerTrees:
            nextLayerTrees = dequeue()

            while layerTrees:
                curTree = layerTrees.popleft()

                if curTree.val == val:
                    return curTree
                if curTree.left is not None:
                    nextLayerTrees.append(curTree.left)
                if curTree.right is not None:
                    nextLayerTrees.append(curTree.right)
            layerTrees = nextLayerTrees

        return None