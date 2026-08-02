class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for index, number in enumerate(nums):
            if number == target:
                return index
        return -1