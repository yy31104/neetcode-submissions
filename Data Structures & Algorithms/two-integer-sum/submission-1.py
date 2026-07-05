class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need not in seen:
                seen[nums[i]] = i
            else:
                return [seen[need],i]