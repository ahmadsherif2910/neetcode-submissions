class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            filtered_row = [digit for digit in board[i] if digit != '.']
            if len(filtered_row) != len(set(filtered_row)):
                return False
        
        for i in range(9):
            col = [row[i] for row in board]
            filtered_col = [digit for digit in col if digit != '.']
            if len(filtered_col) != len(set(filtered_col)):
                return False

        for r in (0, 3, 6):
            for c in (0, 3, 6):
                single_list = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                filtered_box = [digit for digit in single_list if digit != '.']
                if len(filtered_box) != len(set(filtered_box)):
                    return False

        return True