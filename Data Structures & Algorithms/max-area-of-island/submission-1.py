class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0

        def dfs(r, c):
            grid[r][c] = -1
            area = 1

            for dirs in directions:
                nr = r + dirs[0]
                nc = c + dirs[1]

                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1:
                    area += dfs(nr, nc)

            return area


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        
        return ans