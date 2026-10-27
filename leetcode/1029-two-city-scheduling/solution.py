# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        n = len(costs) // 2

        for i in range(n):
            total += costs[i][0]          
            total += costs[i + n][1]      

        return total
                    


