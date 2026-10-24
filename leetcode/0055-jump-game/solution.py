# Runtime: 21 ms
# Memory: 20.5 MB

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= len(nums) - 1:
                return True

        return True
