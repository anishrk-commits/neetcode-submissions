class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            
            if target - number in seen:
                return [seen[target-number], index]

            if number not in seen:
                seen[number] = index
        
            
        