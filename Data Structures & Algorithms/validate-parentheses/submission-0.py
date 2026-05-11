class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        mp = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            if c in mp:
                if stack and stack[len(stack)-1] == mp[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        
        return len(stack) == 0