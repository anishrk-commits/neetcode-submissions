class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = nums[:]
        suffix = nums[:]

        running_product = 1
        for i in range(0, len(nums)):
            prefix[i] = running_product
            running_product *= nums[i]
        
        running_product = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = running_product
            running_product *= nums[i]
        print(suffix)

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output
        


        
        

