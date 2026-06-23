class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        left = 0
        count_t = {}
        count_s = {}
        have = 0
        need = 0
        for ch in t:
            if ch not in count_t:
                count_t[ch] = 0
                need += 1
            count_t[ch] += 1
        for right in range(len(s)):
            ch = s[right]
            count_s[ch] = count_s.get(ch, 0) + 1
            if ch in t and count_s[ch] == count_t[ch]:
                have += 1
            while need == have:
                ch_left = s[left]
                if not ans or right - left + 1 < len(ans):
                    ans = s[left: right + 1]
                if ch_left in count_t:
                    count_s[ch_left] -= 1
                    if count_s[ch_left] < count_t[ch_left]:
                        have -= 1
                else:
                    count_s[ch_left] -= 1
                left += 1
        return ans