# Runtime: 229 ms
# Memory: 19.2 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
    
        max1=0
        ans=''
        if(len(s)==1):
            ans=s
            return ans
        for i in range(len(s)-1):
            a = expand(s,i,i)
            b = expand(s,i,i+1)
            if len(a) > len(ans):
                ans = a
            if len(b) > len(ans):
                ans = b
        return ans
        


        