# Runtime: 11 ms
# Memory: 19.7 MB

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def back(arr, start):
            total = sum(arr)

            if total == target:
                ans.append(arr.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                back(arr, i)  # Reuse the same candidate
                arr.pop()

        back([], 0)
        return ans


