# Runtime: 253 ms
# Memory: 22 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        vis = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            vis[r][c] = 1

            directions = [
                (0, 1),   # right
                (0, -1),  # left
                (1, 0),   # down
                (-1, 0)   # up
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == '1' and
                    vis[nr][nc] == 0):

                    dfs(nr, nc)

        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == '1' and vis[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count



        