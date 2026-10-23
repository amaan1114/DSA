# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
     
        power = abs(n)
        ans = 1.0

        while power:
            if power & 1:
                ans *= x
            x *= x
            power >>= 1

        if n < 0:
            ans = 1.0 / ans

        return ans

