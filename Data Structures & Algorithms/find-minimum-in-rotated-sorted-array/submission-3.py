class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        

        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if(nums[middle] > nums[right]):
                left = middle + 1
            elif(nums[middle] < nums[left]):
                right = middle
            else:
                return nums[left]


        # nums[right]

            