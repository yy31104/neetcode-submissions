class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []
        for ch in s:
            
            if ch in "]})":
                if not stack:
                    return False
                if pair[ch] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(ch)
        return len(stack) == 0
