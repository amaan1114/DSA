# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        def backtrack(arr, i):
            ans.append(arr.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()

        backtrack([], 0)
        return ans