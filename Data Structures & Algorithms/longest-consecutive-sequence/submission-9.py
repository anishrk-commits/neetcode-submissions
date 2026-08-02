class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        clean_nums = sorted(set(nums))

        longest = 1
        record = 1
        if len(clean_nums) == 0:
            return 0
        
        for i in range(0, len(clean_nums)-1):
            if(clean_nums[i] == clean_nums[i+1] - 1):
                longest += 1
            else:
                longest = 1
            
            if(longest > record):
                record = longest
        return record



    

        
                
                