# Runtime: 241 ms
# Memory: 77.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        arr = []
        def dfs(node,l):
            if(node == None):
                return
            if(len(arr)>l):
                arr[l]+=node.val
            else:
                arr.append(node.val)
            dfs(node.left,l+1)
            dfs(node.right,l+1)
        dfs(root,0)
        arr.sort()
        if(len(arr)>=k):
            return arr[-k]
        else:
            return -1
        


            