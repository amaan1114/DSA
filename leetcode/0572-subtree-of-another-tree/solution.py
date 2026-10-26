# Runtime: 72 ms
# Memory: 20.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isIdentical(s,t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False

            return (s.val == t.val and
                    isIdentical(s.left, t.left) and
                    isIdentical(s.right, t.right))
        if subRoot is None:
            return True
        if root is None:
            return False

        if isIdentical(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
