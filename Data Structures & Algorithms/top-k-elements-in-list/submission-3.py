class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        for i in range(len(nums), 0, -1):
            for num in  buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            
        

        


            