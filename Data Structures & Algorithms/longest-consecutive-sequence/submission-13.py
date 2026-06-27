class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            if num - 1 not in seen:
                best = 1
                n = num 
                while n + 1 in seen:
                    best += 1
                    n += 1
                ans = max(ans, best)
        return ans
