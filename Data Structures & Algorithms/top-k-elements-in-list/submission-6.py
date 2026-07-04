class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        l = [[] for _ in range(len(nums) + 1)]
        for num,freq in count.items():
            l[freq].append(num)
        for i in range(len(nums), -1, -1):
            if l[i]:
                for n in l[i]:
                    if len(ans) < k:
                        ans.append(n)
        return ans
