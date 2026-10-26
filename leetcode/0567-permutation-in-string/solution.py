# Runtime: 1664 ms
# Memory: 19.3 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr=[0]*26
        st=0
        end = len(s1)
        for i in s1:
            arr[ord(i)-97]+=1
        while end<=len(s2):
            s3 = s2[st:end]
            temp = [0] * 26
            for i in s3:
                temp[ord(i)-97]+=1
            if(arr==temp):
                return True
            st +=1
            end +=1
     
        return False

