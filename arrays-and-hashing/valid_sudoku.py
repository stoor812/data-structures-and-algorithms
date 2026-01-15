from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check Each Row contains no duplicates
        for i in range(len(board)):
            rowSeen = set()
            for j in range (len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowSeen:
                    return False
                else:
                    rowSeen.add(board[i][j])
        
        # Check Each Column contains no duplicates
        for i in range(len(board)):
            colSeen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in colSeen:
                    return False
                else:
                    colSeen.add(board[j][i])
        
        # Check Each Box contains no duplicates
        for square in range(9):
            boxSeen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in boxSeen:
                        return False
                    else:
                        boxSeen.add(board[row][col])

        return True

"""
Approach:
- Validate rows: for each row, use a set to detect duplicates (ignore '.')
- Validate columns: for each column, use a set to detect duplicates (ignore '.')
- Validate 3x3 boxes: iterate over the 9 boxes and use a set to detect duplicates
  (map each box index to its 3x3 coordinates)

Time Complexity: O(n^2) for a standard 9x9 Sudoku (always 81 cells checked a constant number of times)
Space Complexity: O(n) for a standard 9x9 Sudoku (sets hold at most 9 values each)
Difficulty: Medium
"""


