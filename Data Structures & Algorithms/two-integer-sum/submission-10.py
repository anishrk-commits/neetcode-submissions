class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # seen = {}
       # for index, num in enumerate(nums):
       #     
       #     if(target - num in seen):
       #         return [seen[target-num], index]
       #     
       #     seen[num] = index
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
