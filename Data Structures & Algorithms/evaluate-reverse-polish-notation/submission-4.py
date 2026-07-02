class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == '+':
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(second_num + first_num)
            elif tok == '-':
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(second_num - first_num)
            elif tok == '*':
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(second_num * first_num)
            elif tok == '/':
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(int(second_num / first_num))
            else:
                stack.append(int(tok))
        
        return stack[0]