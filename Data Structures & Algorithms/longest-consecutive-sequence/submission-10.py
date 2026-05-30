class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        ans = 0
        for n in num:
            if n - 1 not in num:
                length = 1
                while n + length in num:
                    length += 1
                ans = max(ans, length)
        return ans
        
    