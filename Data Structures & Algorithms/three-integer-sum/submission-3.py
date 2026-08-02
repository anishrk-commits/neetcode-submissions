class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if len(nums) == 3:
            sum = 0
            for number in nums:
                sum += number
            if sum == 0:
                answer.append(nums)
                return answer
            else:
                return answer
        
        nums.sort() #O(nlogn)

        answer = []


        for pivot in range(len(nums)-2):
            if nums[pivot] == nums[pivot - 1] and pivot != 0:
                continue
            right = len(nums) - 1
            left = pivot + 1
            while True:
                if(left >= right):
                    break
                elif(nums[pivot] + nums[left] + nums[right] == 0):
                    answer.append([nums[pivot],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right += -1
                elif(nums[pivot] + nums[left] + nums[right] > 0):
                    right += -1
                else:
                    left += 1
        return answer
        # -4, -1, -1, 0, 1 ,2



        
