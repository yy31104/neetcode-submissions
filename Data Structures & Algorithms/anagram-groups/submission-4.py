class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)
        return list(ans.values())

            
