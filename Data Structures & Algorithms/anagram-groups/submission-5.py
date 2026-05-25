class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26

            for ch in s:
                index = ord(ch) - ord("a")
                count[index] += 1

            key = tuple(count)
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)
        return list(ans.values())

            
