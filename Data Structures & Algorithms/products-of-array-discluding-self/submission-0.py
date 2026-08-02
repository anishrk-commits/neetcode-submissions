class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 3] -> [6, 3, 2]
        # number
        output = nums[:]
        product = 1

        print(output)
        zero_counter = 0
        
        for number in nums:
            if(number == 0):
                zero_counter += 1
                continue
            else:
                product *= number

        for i in range(len(nums)):
            if(nums[i] == 0 and zero_counter <= 1):
                output[i] = product
            elif(nums[i] == 0 and zero_counter > 1):
                output[i] = 0
            elif(nums[i] != 0 and zero_counter != 0):
                output[i] = 0
            else:
                output[i] = int(product / nums[i])
        return output


