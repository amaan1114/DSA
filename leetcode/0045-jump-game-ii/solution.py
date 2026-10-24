# Runtime: 3 ms
# Memory: 20.1 MB

class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                jumps += 1
                currentEnd = farthest

        return jumps