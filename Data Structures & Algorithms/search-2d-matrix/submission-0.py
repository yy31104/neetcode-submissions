class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            val = matrix[r][c]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False
                
