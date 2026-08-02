class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1

        while left <= right:
            middle = (left + right) // 2
            if(matrix[middle][0] == target):
                return True
            elif(matrix[middle][0] > target):
                right = middle - 1
            else:
                left = middle + 1
        
        index = right
        left = 0
        right = len(matrix[index]) - 1
        print(index)
        while left <= right:
            middle = (left + right) // 2
            if(matrix[index][middle] == target):
                return True
            elif(matrix[index][middle] > target):
                right = middle - 1
            else:
                left = middle + 1
        
        return False




