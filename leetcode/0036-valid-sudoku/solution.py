# Runtime: 5 ms
# Memory: 19.3 MB

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:    
        def check(col,row,value):
            count=0
            for i in range(9):
                if(board[i][row]==value):
                    count+=1
            for j in range(9):
                if(board[col][j]==value):
                    count+=1
            row = row-(row%3)
            col = col-(col%3)
            for i in range(col,col+3):
                for j in range(row,row+3):
                    if(board[i][j]==value):
                        count+=1
            if(count>3):
                return False
            return True
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j]=='.'):
                    continue
                elif(not check(i,j,board[i][j])):
                    return False
        return True