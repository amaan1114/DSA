# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(arr,i):
            if(i==len(nums)):
                ans.append(arr.copy())
                return
            arr.append(nums[i])
            
            backtrack(arr,i+1)
            arr.pop()
            backtrack(arr,i+1)
        backtrack([],0)
        return ans
            
                
            