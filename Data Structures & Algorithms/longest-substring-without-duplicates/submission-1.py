class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        left = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            ans = max(ans, r - left + 1)
        return ans



            
