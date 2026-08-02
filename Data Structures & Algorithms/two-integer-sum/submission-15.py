class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, value in enumerate(nums):
            remainder = target - value

            if remainder in seen:
                return [seen[remainder],index]
            if value not in seen:
                seen[value] = index

        return []