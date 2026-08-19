class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return False
        
        tracker = set()

        for number in nums:
            if number in tracker:
                return True
            else:
                tracker.add(number)
        
        return False
