class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count_s = {}
        need = 0
        have = 0
        left = 0
        ans = ""
        best = float("inf")
        for ch in t:
            if ch not in count_t:
                count_t[ch] = 0
                need += 1
            count_t[ch] += 1
        for right in range(len(s)):
            ch = s[right]
            if ch not in count_s:
                count_s[ch] = 0
            count_s[ch] += 1
            if ch in count_t and count_t[ch] == count_s[ch]:
                have += 1
            while need == have:
                best = min(best, right - left + 1)
                if right - left + 1 == best:
                    ans = s[left: right + 1]
                left_ch = s[left]
                if left_ch in count_t:
                    count_s[left_ch] -= 1
                    if count_t[left_ch] > count_s[left_ch]:
                        have -= 1
                left += 1
        return ans
                    
        



        