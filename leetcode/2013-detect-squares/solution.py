# Runtime: 122 ms
# Memory: 21 MB

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        ans = 0

        for (x2, y2), freq in self.points.items():

            if x == x2 or y == y2:
                continue

            if abs(x - x2) == abs(y - y2):

                p1 = (x2, y)
                p2 = (x, y2)

                ans += freq * self.points.get(p1, 0) * self.points.get(p2, 0)

        return ans