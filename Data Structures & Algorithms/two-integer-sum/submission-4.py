class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        difference = {value: index for index, value in enumerate(nums)} 

        for i in nums:
            
            if(difference.get(target - i) == None):
                continue
            elif(difference.get(target - i) == nums.index(i)):
                continue
            else:
                answer.append(nums.index(i))
                answer.append(difference.get(target - i))
                return answer
