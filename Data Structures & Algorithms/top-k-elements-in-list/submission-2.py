class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        for i in range(len(nums), 0, -1):
            if len(ans) < k:
                for num in buckets[i]:
                    ans.append(num)
        return ans



            
        

        


            