# Runtime: 45 ms
# Memory: 26.8 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def f(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if((i,j) in dp):
                return dp[(i,j)]
            if word1[i] == word2[j]:
                dp[(i,j)] = f(i + 1, j + 1)
            else:
                insert = 1 + f(i, j + 1)

                delete = 1 + f(i + 1, j)

                replace = 1 + f(i + 1, j + 1)

                dp[(i,j)] = min(insert, delete, replace)
            return dp[(i,j)]
        return f(0, 0)




