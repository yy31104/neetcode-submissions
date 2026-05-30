class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for ch in s1:
            num = ord(ch) - ord("a")
            count1[num] += 1
        left = 0
        for right in range(n):
            num = ord(s2[right]) - ord("a")
            idx = ord(s2[left]) - ord("a")
            count2[num] += 1
            if right - left + 1 > m:
                count2[idx] -= 1
                left += 1
            if right - left + 1 == m:
                if count1 == count2:
                    return True
        return False
                


