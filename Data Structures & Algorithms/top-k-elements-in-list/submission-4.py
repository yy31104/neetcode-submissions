class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        order = [[] for _ in range(len(nums) + 1)]
        ans = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n,freq in count.items():
            order[freq].append(n)
        for i in range(len(nums), 0, -1):
            if order[i] and len(ans) < k:
                for num in order[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans

