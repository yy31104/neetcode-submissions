class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        ans = float("inf")
        for pile in piles:
            max_pile = max(max_pile, pile)
        left = 1
        right = max_pile
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            if time <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

