# Runtime: 26 ms
# Memory: 19.5 MB

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        def back(arr,start):
            sum1 = sum(arr)
            if(sum1==target):
                ans.append(arr.copy())
                return
            if(sum1>target):
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                back(arr,i+1)
                arr.pop()
        back([],0)
        return ans