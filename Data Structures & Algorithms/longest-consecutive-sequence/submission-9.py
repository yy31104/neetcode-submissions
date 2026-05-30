class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            ans = 0
            num = set()
            for n in nums:
                num.add(n)
            for n in num:
                if n - 1 not in num:
                    length = 1
                    while n + length in num:
                        length += 1
                    ans = max(ans, length)
        return ans
        
    