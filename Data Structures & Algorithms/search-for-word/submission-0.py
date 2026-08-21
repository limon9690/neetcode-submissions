class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        l = len(word)
        path = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(word, i, r, c):
            if l == i:
                return True

            if r >= n or c >= m or r < 0 or c < 0 or board[r][c] != word[i] or (r, c) in path:
               return False

            path.add((r, c))

            for dirs in directions:
                nr, nc = r + dirs[0], c + dirs[1]
                if dfs(word, i+1, nr, nc):
                    return True

            path.remove((r, c))

            return False

        
        for r in range(n):
            for c in range(m):
                if dfs(word, 0, r, c):
                    return True

        return False