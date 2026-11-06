# Runtime: 4955 ms
# Memory: 19.3 MB

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ans = [False]

        def backtrack(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found = (
                backtrack(i+1, j, k+1) or
                backtrack(i-1, j, k+1) or
                backtrack(i, j+1, k+1) or
                backtrack(i, j-1, k+1)
            )

            board[i][j] = temp

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False