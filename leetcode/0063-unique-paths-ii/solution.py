# Runtime: 1 ms
# Memory: 19.6 MB

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp={}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def f(i,j):
            if(i==m-1 and j==n-1 and obstacleGrid[i][j]!=1):
                return 1
            if(i>=m or j>=n):
                return 0
            if(obstacleGrid[i][j]==1):
                return 0
            if((i,j) in dp):
                return dp[(i,j)]
            right = f(i+1,j)
            down = f(i,j+1)
            dp[(i,j)] = right+down
            return dp[(i,j)]
        return f(0,0)