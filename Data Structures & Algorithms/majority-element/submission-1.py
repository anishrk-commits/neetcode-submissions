class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = None
        count = 0

        for number in nums:
            if majority is None:
                majority = number
                count += 1
                continue
            
            if number == majority:
                count += 1
            else:
                count -= 1

            if count == 0:
                majority = number
                count += 1
        return majority

            