class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count_s = {}
        need = 0
        for ch in t:
            if ch not in count_t:
                count_t[ch] = 0
                need += 1
            count_t[ch] += 1
        have = 0
        left = 0
        ans = ""
        best = float("inf")
        for right in range(len(s)):
            ch = s[right]
            if ch not in count_s:
                count_s[ch] = 0
            count_s[ch] += 1
            if ch in t and count_t[ch] == count_s[ch]:
                have += 1
            while need == have:
                if right - left + 1 < best:
                    best = right - left + 1
                    ans = s[left:right + 1]
                count_s[s[left]] -= 1
                if s[left] in t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        return ans
                


            