class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        r, c = 0, col-1
        while r < row and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target: #get rid of column c
                c -= 1
            else:
                r += 1
        return False
            
                
        