# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[-1]*(n+1)
        def transv(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1

            elif arr[n] != -1:
                return arr[n]
            else:
                arr[n] = transv(n-3) + transv(n-2) + transv(n-1)
                return arr[n]

        return transv(n)
