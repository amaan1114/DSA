# Runtime: 11 ms
# Memory: 20.1 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []

        for i in s.lower():
            if(97<=ord(i)<=122 or 48<=ord(i)<=57):
                l.append(i)
        ans = "".join(l)
        print(ans)
        left=0
        right=len(ans)-1
        while left<=right:
            if(ans[left]==ans[right]):
                left+=1
                right-=1
            else:
                return False
        return True

