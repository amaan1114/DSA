# Runtime: 2600 ms
# Memory: 500.6 MB

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}

        def f(i, buy, transactions):
            if i >= len(prices) or transactions == 0:
                return 0

            if (i, buy, transactions) in memo:
                return memo[(i, buy, transactions)]

            if buy:
                take = -prices[i] + f(i+1, 0, transactions)
                skip = f(i+1, 1, transactions)
            else:
                take = prices[i] + f(i+1, 1, transactions-1)
                skip = f(i+1, 0, transactions)

            memo[(i, buy, transactions)] = max(take, skip)

            return memo[(i, buy, transactions)]

        return f(0, 1, 2)