# Runtime: 1 ms
# Memory: 19.6 MB

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def back(arr):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in arr:
                    continue

                arr.append(nums[i])
                back(arr)
                arr.pop()

        back([])
        return ans

            