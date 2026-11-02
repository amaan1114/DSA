# Runtime: 4 ms
# Memory: 20.5 MB

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        num1 = nums[len(nums)//2]
        count=0
        for i in nums:
            count+=abs(num1-i)
        return count