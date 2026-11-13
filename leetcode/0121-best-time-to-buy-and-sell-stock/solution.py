# Runtime: 37 ms
# Memory: 28.5 MB

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max1 = 0

        for i in prices:
            if i < buy:
                buy = i
            else:
                max1 = max(max1, i - buy)

        return max1



