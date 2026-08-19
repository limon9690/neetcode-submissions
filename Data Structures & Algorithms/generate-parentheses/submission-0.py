class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                dfs(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                dfs(opened, closed + 1)
                stack.pop()

        
        dfs(0, 0)

        return res
