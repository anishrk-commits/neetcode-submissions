class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = set()

        left = 0
        right = left + 1
        length = len(nums)
        while right < length:
            if nums[left] == nums[right]:
                nums.remove(nums[right])
                length -= 1
                continue
            left = right
            right += 1
        
        return len(nums)