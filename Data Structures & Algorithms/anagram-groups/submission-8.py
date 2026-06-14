class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            key = [0] * 26
            for ch in s:
                index = ord(ch) - ord("a")
                key[index] += 1
            key = tuple(key)
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        return list(ans.values())



                

                