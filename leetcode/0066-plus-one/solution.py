# Runtime: 0 ms
# Memory: 19 MB

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans=[]
        digit=0
        for i in digits:
            digit+=i
            digit = digit*10
        ansval = (digit//10)+1
        while ansval!=0:
            ans.append(ansval%10)
            ansval//=10
        return ans[::-1]
