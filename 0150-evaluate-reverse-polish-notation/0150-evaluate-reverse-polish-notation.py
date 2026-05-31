class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))  # truncate toward 0

            else:
                stack.append(int(token))

        return stack[-1]