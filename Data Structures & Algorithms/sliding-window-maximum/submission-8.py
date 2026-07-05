class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        from collections import deque
        dq = deque()
        for right in range(len(nums)):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            dq.append(right)
            left = right - k + 1
            if left > dq[0]:
                dq.popleft()
            if right >= k - 1:
                ans.append(nums[dq[0]])
        return ans

