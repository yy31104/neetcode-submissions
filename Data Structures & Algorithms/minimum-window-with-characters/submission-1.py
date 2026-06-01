class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = float("inf")
        left = 0
        count_t = {}
        count_s = {}
        ans = ""
        have = 0
        for i in t:
            if i not in count_t:
                count_t[i] = 0
            count_t[i] += 1
        need = len(count_t)
        for right in range(len(s)):
            ch = s[right]
            if ch in count_t:
                count_s[ch] = count_s.get(ch, 0) + 1
                if count_t[ch] == count_s[ch]:
                    have += 1

            while need == have:
                if best > right - left + 1:
                        best = right - left + 1
                        ans = s[left: right + 1]
                if s[left] in count_s:
                    count_s[s[left]] -= 1
                    if count_s[s[left]] < count_t[s[left]]:
                        have -= 1
                left += 1
        return ans


                    


            

        

