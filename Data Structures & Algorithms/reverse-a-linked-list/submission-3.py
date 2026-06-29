class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []
        for ch in s:
            if not stack:
                if ch not in "({[":
                    return False
                else:
                    stack.append(ch)
            else:
                if ch in "]})":
                    if stack[-1] != pairs[ch]:
                        return False
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack) == 0
            