# Runtime: 0 ms
# Memory: 19.5 MB


import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert into max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # Heaviest
            x = -heapq.heappop(stones)  # Second heaviest

            if x != y:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0
