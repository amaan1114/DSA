# Runtime: 95 ms
# Memory: 19.4 MB

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def check(par):
            arr=[]
            for i in par:
                if(len(arr)==0):
                    arr.append(i)
                    continue
                if(arr[-1]=='(' and i==')'):
                    arr.pop()
                else:
                    arr.append(i)
            if(len(arr)==0):
                return True
            else:
                return False
                        
        ans = []
        bracks=[]
        string="()"

        def back(arr,string):
            if(len(arr)==n*2):
                if(check(arr)):
                    ans.append("".join(arr))
                return
            for i in string:
                arr.append(i)
                back(arr,string)
                arr.pop()
        back([],string)

        return ans