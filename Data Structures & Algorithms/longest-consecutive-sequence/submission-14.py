class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        starters = []

        if(len(nums) ==  0):
            return 0
        
        for number in nums:
            if(number + 1 in seen and number - 1 in seen):
                continue
            elif(number + 1 in seen):
                starters.append(number)

        if(len(starters) == 0):
            return 1
        print(starters)
        longest = 2
        record = 2
        for number in starters:
            i = 2
            longest = 2
            while True:
                if(number + i in seen):
                    longest += 1
                    i += 1
                    if(longest > record):
                        record = longest
                else:
                    break
        return record



