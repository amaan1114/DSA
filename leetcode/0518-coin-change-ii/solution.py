# Runtime: 2093 ms
# Memory: 373.9 MB

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}
        def f(i,target):
            if(target==0):
                return 1
            if(i==len(coins)):
                return 0
            if((i,target) in memo):
                return memo[(i,target)]
            pick=0

            if(target>=coins[i]):
                pick = f(i,target-coins[i])
            skip = f(i+1,target)
            memo[(i,target)]=pick+skip
            return memo[(i,target)]
        return f(0,amount)

