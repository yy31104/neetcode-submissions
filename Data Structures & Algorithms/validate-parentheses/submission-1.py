class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        for ch in s:
            if not stack and ch not in "[{(":
                return False
            if ch in "[{(":
                stack.append(ch)
            else:
                if stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
        