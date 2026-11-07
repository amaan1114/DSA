# Runtime: 449 ms
# Memory: 83.9 MB

class Solution:
    def closestNodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
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
            left, right = 0, len(nums) - 1
            mini, maxi = -1, -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == q:
                    mini = maxi = nums[mid]
                    break

                elif nums[mid] < q:
                    mini = nums[mid]
                    left = mid + 1

                else:
                    maxi = nums[mid]
                    right = mid - 1

            ans.append([mini, maxi])

        return ans