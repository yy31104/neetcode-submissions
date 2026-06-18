class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        max_freq = 0
        count = [0] * 26
        for right in range(len(s)):
            r = ord(s[right]) - ord("A")
            count[r] += 1
            max_freq = max(max_freq, count[r])
            while right - left + 1 - max_freq > k:
                l = ord(s[left]) - ord("A")
                count[l] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans