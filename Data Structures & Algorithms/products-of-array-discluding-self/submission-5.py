class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer = []
        for i in range(0, len(nums), 1):
            answer.append(prefix)
            prefix *= nums[i]
        
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
#  [1, 1, 2, 8] p
#  [48, 24, 6, 1] s
#  [48, 24, 12, 8] answer
