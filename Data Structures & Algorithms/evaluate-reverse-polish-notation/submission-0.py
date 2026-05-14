class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in '+-*/':
                stack.append(int(c))
            else:
                x1 = stack.pop()
                x2 = stack.pop()

                if c == '+':
                    stack.append(x1 + x2)
                elif c == '-':
                    stack.append(x2 - x1)
                elif c == '*':
                    stack.append(x1 * x2)
                else:
                    stack.append(int(x2 / x1))
                

        return stack[0]