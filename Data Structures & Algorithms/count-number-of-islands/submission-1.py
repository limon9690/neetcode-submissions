class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total = 0

        def dfs(r, c):
            grid[r][c] = "0"

            for dirs in directions:
                nr = r + dirs[0]
                nc = c + dirs[1]

                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == "1":
                    dfs(nr, nc)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total += 1

        
        return total