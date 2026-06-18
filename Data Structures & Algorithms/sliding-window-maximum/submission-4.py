class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        ans = []
        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            left = right - k + 1
            if dq[0] < left:
                dq.popleft()
            if left >= 0:
                ans.append(nums[dq[0]])
        return ans

