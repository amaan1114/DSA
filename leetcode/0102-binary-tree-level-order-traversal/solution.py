# Runtime: 0 ms
# Memory: 20.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        arr={}
        ans=[]
        def traverse(root,lvl):
            if(root ==None):
                return 
            if(lvl in arr):
                arr[lvl].append(root.val)
            else:
                arr[lvl]=[root.val]
            traverse(root.left,lvl+1)
            traverse(root.right,lvl+1)
        traverse(root,0)
        for i in arr:
            ans.append(arr[i])
        return ans


