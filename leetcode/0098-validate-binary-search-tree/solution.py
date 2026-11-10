# Runtime: 3 ms
# Memory: 20.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        arr=[]
        def inorder(root):
            if(root==None):
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
       
        for i in range(len(arr)-1):
            if(arr[i]>=arr[i+1]):
                return False
            
        return True

