class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in ["+", "-", "*", "/"]:
                stack.append(int(n))
            else:
                right = stack.pop()
                left = stack.pop()
                if n == "+":
                    stack.append(left + right)
                if n == "-":
                    stack.append(left - right)
                if n == "*":
                    stack.append(left * right)
                if n == "/":
                    stack.append(int(left / right))
        return stack[-1]