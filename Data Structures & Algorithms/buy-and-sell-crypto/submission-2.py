class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = float("inf")
        for price in prices:
            l = min(l, price)
            ans = max(ans, price - l)
        return ans