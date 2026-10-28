# Runtime: 3 ms
# Memory: 19.4 MB

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hasht = {}
        for i in range(len(s)):
            hasht[s[i]] = i
        ans=[]
        start=0
        end=0
        for i in range(len(s)):
            end = max(end, hasht[s[i]])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
            

            
                



