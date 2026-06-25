class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = height[0]
        suffix[len(height) - 1] = height[len(height) - 1]
        ans = 0
        for i in range(1, len(height)):
            if height[i] > prefix[i - 1]:
                prefix[i] = height[i]
            else:
                prefix[i] = prefix[i - 1]
        for i in range(len(height) - 2, -1, -1):
            if height[i] > suffix[i + 1]:
                suffix[i] = height[i]
            else:
                suffix[i] = suffix[i + 1]
        for i in range(len(height)):
            ans += min(suffix[i], prefix[i]) - height[i]
        return ans
        