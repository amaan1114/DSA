# Runtime: 1 ms
# Memory: 19.2 MB

class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        xcop = x
        x = abs(x)
        while x>0:
            lastval = x%10
            ans=ans*10+lastval
            x//=10
        if(xcop<0):
            if(-ans<-2147483648):
                return 0
            return -ans
        if(ans>2147483647):
            return 0
        return ans



