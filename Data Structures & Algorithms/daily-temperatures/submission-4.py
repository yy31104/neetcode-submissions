class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for right in range(len(temperatures)):
            while stack and temperatures[right] > temperatures[stack[-1]]:
                ans[stack[-1]] = right - stack[-1]
                stack.pop()
            stack.append(right)
        return ans

      