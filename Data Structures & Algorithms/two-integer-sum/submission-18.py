class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in lookup:
                return [lookup[remainder], index]
            
            if value not in lookup:
                lookup[value] = index
        