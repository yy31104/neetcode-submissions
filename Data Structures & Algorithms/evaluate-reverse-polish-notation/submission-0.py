class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                right = stack.pop()
                left = stack.pop()
                if ch == "+":
                    stack.append(left + right)
                if ch == "-":
                    stack.append(left - right)
                if ch == "*":
                    stack.append(left * right)
                if ch == "/":
                    stack.append(int(left / right))
        return stack[-1]

        