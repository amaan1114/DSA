# Runtime: 4 ms
# Memory: 20.2 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def backtrack(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j

            if k == len(s3):
                return True

            ans = False

            if i < len(s1) and s1[i] == s3[k]:
                ans = backtrack(i + 1, j)

            if not ans and j < len(s2) and s2[j] == s3[k]:
                ans = backtrack(i, j + 1)

            memo[(i, j)] = ans

            return ans

        return backtrack(0, 0)