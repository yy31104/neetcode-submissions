class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_count = {}
        window_count = {}
        need = 0
        have = 0
        for ch in t:
            if ch not in need_count:
                need_count[ch] = 0
                need += 1
            need_count[ch] += 1
        left = 0
        res_len = float("inf") 
        res = [-1, -1]
        for right in range(len(s)):
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1
            if ch in need_count and window_count[ch] == need_count[ch]:
                have += 1
            while need == have:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = [left, right]
                left_ch = s[left]
                window_count[left_ch] -= 1
                if left_ch in need_count and window_count[left_ch] < need_count[left_ch]:
                    have -= 1
                left += 1
        if res_len == float("inf"):
            return ""
        l, r = res
        return s[l:r + 1]
            

        

