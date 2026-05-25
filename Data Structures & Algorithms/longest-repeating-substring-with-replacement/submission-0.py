class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0 
        freq = {}
        maxFreq = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            window_length = right - left + 1
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
                maxFreq = max(freq.values())
            ans = max(ans, right - left + 1)
        return ans
