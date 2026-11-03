# Runtime: 4 ms
# Memory: 19.2 MB

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in nums:
            count+=nums[-1]-i
        return count

