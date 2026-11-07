# Runtime: 159 ms
# Memory: 82.5 MB

from bisect import bisect_left

class Solution:
    def closestNodes(self, root, queries):
        nums = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        ans = []

        for q in queries:
            i = bisect_left(nums, q)

            if i < len(nums) and nums[i] == q:
                ans.append([q, q])
            else:
                mini = nums[i - 1] if i > 0 else -1
                maxi = nums[i] if i < len(nums) else -1

                ans.append([mini, maxi])

        return ans