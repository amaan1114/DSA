# Runtime: 4 ms
# Memory: 19.2 MB

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minute=0
        while True:
            rotten = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if(grid[i][j]==1):
                        if(j>0):
                            if(grid[i][j-1]==2):
                               rotten.append((i,j))
                        if(j<len(grid[i])-1):
                            if(grid[i][j+1]==2):
                                rotten.append((i,j))
                        if(i>0):
                            if(grid[i-1][j]==2):
                                rotten.append((i,j))
                        if(i<len(grid)-1):
                            if(grid[i+1][j]==2):
                                rotten.append((i,j))
            if(len(rotten)==0):
                break
            for i,j in rotten:
                grid[i][j]=2
            minute+=1
        for i in grid:
            for j in i:
                if(j==1):
                    return -1
        return minute
                           


