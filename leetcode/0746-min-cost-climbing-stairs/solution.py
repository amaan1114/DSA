# Runtime: 9 ms
# Memory: 20.8 MB

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
            n = len(cost)
            dp=[-1]*(n+1)
            def jump(i):
                if(i<=1):
                    return 0
                if(dp[i]!=-1):
                    return dp[i]
                climb1 = jump(i-1)+cost[i-1]
                climb2 = jump(i-2)+cost[i-2]
                ans = min(climb1,climb2)
                dp[i] = ans
                return dp[i]
            return jump(n)