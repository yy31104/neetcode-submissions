class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for ch in s:
            if not stack and ch not in "[{(":
                return False
            if ch in "[{(":
                stack.append(ch)
            if ch in "]})":
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
        