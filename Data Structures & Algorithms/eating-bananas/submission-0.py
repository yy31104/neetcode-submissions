class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        ans = float("inf")
        for pile in piles:
            max_pile = max(max_pile, pile)
        l = 1
        r = max_pile
        while l <= r:
            med = (l + r) // 2
            time = 0
            for pile in piles:
                time += (pile + med - 1) // med
            if time > h:
                l = med + 1
            else:
                r = med - 1
                ans = min(ans, med)
        return ans
                