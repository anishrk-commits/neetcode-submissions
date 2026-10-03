class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            if i != len(mat) - i - 1:
                sum += mat[i][len(mat) - i - 1]
            sum += mat[i][i]
    
        return sum