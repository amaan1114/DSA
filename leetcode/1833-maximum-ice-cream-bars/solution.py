# Runtime: 85 ms
# Memory: 32.1 MB

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in costs:
            coins-=i
            if(coins>=0):
                count+=1
            else:
                break
        return count