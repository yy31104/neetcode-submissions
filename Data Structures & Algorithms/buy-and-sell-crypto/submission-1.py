class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr = prices[0]
        for n in prices:
            curr = min(curr, n)
            ans = max(ans,n - curr)
        return ans



      