class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        best = 0
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)
            stack.append(i)
            
        for i in range(len(heights)):
            area = (right[i] - left[i] - 1) * heights[i]
            best = max(area, best)
        return best


