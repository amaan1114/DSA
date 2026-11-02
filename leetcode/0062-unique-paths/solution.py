# Runtime: 2 ms
# Memory: 20.2 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def f(i,j):
            if i==m-1 and j==n-1:
                return 1
            if((i,j) in memo):
                return memo[(i,j)]
            down = 0
            right =0
            if(i<m):
                down = f(i+1,j)
            if(j<n):
                right = f(i,j+1)
            memo[(i,j)]=down+right
            return memo[(i,j)]
        return f(0,0)