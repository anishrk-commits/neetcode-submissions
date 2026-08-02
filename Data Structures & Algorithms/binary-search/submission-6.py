class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = int((right + left) / 2)
        
        while True:
            if nums[middle] == target:
                return middle
            elif nums[right] == target:
                return right
            elif left == middle or right == middle:
                return -1
            elif target < nums[middle]:
                right = middle
                middle = int((left + right) / 2)
            else:
                left = middle
                middle = int((left + right) / 2)


                
