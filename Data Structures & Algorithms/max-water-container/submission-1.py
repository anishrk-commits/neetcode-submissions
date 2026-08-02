class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        if(left == right and heights[left] < heights[right]):
            return heights[left]
        elif(left == right and heights[left] < heights[right]):
            return heights[right]

        most = 0

        while True:
            if(left >= right):
                return most
            elif(heights[left] < heights[right]):
                amount = heights[left] * (right - left)
                if(amount > most):
                    most = amount
                left += 1
            elif(heights[left] > heights[right]):
                amount = heights[right] * (right - left)
                if(amount > most):
                    most = amount
                right += -1
            else:
                amount = heights[left] * (right - left)
                if(amount > most):
                    most = amount
                if(heights[left + 1] > heights[right - 1]):
                    left += 1
                else:
                    right += -1


        
            