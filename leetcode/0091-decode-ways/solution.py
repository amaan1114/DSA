# Runtime: 1 ms
# Memory: 19.4 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def backtrack(i):
            if i == len(s):
                return 1

            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            ans = backtrack(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ans += backtrack(i + 2)

            dp[i] = ans
            return ans

        return backtrack(0)
            

