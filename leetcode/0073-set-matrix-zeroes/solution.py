# Runtime: 233 ms
# Memory: 24 MB

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        cols=len(matrix[0])
        rows = len(matrix)
        arr=[]
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j]==0):
                    arr.append([i,j])
        print(arr)
        for r, c in arr:
            for j in range(cols):
                matrix[r][j] = 0

            for i in range(rows):
                matrix[i][c] = 0
        