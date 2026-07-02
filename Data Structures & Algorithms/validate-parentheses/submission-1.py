class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            elif len(stack) > 0:
                prev = stack[-1]

                if c == ')' and prev == '(':
                    stack.pop()
                elif c == ']' and prev == '[':
                    stack.pop()
                elif c == '}' and prev == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0