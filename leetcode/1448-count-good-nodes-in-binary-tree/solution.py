# Runtime: 130 ms
# Memory: 31.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max1):
            if node is None:
                return 0

            count = 0

            if node.val >= max1:
                count = 1
                max1 = node.val

            count += dfs(node.left, max1)
            count += dfs(node.right, max1)

            return count
        return dfs(root,float('-inf'))
        

        