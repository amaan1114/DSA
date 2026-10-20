# Runtime: 52 ms
# Memory: 29.6 MB

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max1 = 0
        low=0
        high = len(height)-1
        while low<high:
            arr = (high-low)*min(height[low],height[high])
            if(arr>max1):
                max1=arr
            if(height[low]<height[high]):
                low+=1
            else:
                high-=1
        return max1
        