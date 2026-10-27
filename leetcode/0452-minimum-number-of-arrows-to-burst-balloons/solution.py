# Runtime: 73 ms
# Memory: 53.3 MB

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        over=0
        prev = points[0][1]
        for i in range(1,len(points)):
            if(prev>=points[i][0]):
                over+=1
            else:
                prev = points[i][1]
        return len(points)-over