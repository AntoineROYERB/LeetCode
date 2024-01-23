#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = len(board)

        # Check each row for repetition
        for i in range(N):
            temp_row = [case for case in board[i] if case != '.']
            set_row = set(temp_row)
            if len(set_row) != len(temp_row):
                return False

        # Check each column for repetition
        for i in range(N):
            temp_column = [board[j][i] for j in range(N) if board[j][i] != '.']
            set_column = set(temp_column)
            if len(set_column) != len(temp_column):
                return False

        # Check each sub-square for repetition
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                temp_sub_square = []
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != '.':
                            temp_sub_square.append(board[i + k][j + l])

                set_sub_square = set(temp_sub_square)
                if len(set_sub_square) != len(temp_sub_square):
                    return False

        # If no repetition found, the board is valid
        return True