class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pre = [-1] * n
        suf = [n] * n
        ans = 0
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            pre[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            suf[i] = stack[-1] if stack else n
            stack.append(i)
        for i in range(n):
            area = (suf[i] - pre[i] - 1) * heights[i]
            ans = max(ans, area)
        return ans
            
