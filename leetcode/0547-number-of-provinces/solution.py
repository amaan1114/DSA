# Runtime: 8 ms
# Memory: 21.2 MB

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
    
        vis = [False]*n
        def dfs(node):
            vis[node]=True
            for neighbour in adj[node]:
                if not vis[neighbour]:
                    dfs(neighbour)
        c=0
        for node in range(n):
            if not vis[node]:
                dfs(node)
                c+=1
        return c
    
