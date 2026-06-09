class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count1 = [0] * 26
        count2 = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord("a")
            count1[idx] += 1
        for right in range(len(s2)):
            idx_right = ord(s2[right]) - ord("a")
            count2[idx_right] += 1
            if right - left + 1 > len(s1):
                idx_left = ord(s2[left]) - ord("a")
                count2[idx_left] -= 1
                left += 1
            if right - left + 1 == len(s1):
                if count1 == count2:
                    return True
        return False




            
            
            
            