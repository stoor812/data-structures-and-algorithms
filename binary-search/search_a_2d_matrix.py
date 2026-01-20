from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows*cols - 1

        while left <= right:
            middle = (left + right) // 2
            # Convert to 2D MATRIX
            m1 = middle // cols
            m2 = middle % cols
            if matrix[m1][m2] < target:
                # Target is less than search left
                left = middle + 1
            elif matrix[m1][m2] > target:
                # Target is greater than search right
                right = middle - 1
            else:
                return True

        return False
    
"""
Approach:
- Treat the 2D matrix as a flattened 1D sorted array
- Perform binary search over indices from 0 to rows * cols - 1
- Convert the 1D index to 2D coordinates using:
    row = index // number_of_columns
    col = index % number_of_columns
- Compare the matrix value at (row, col) with the target to adjust search range

Time Complexity: O(log(m * n))
Space Complexity: O(1)
Difficulty: Medium
"""
