class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, counter):
            nonlocal ans
            grid[r][c] = -1
            counter[0] += 1

            ans = max(ans, counter[0])

            for dirs in directions:
                nr = r + dirs[0]
                nc = c + dirs[1]

                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1:
                    dfs(nr, nc, counter)


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dfs(r, c, [0])

        return ans