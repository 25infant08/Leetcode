class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[''] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return 'A' if board[i][0] == 'X' else 'B'
            if board[0][i] == board[1][i] == board[2][i] != '':
                return 'A' if board[0][i] == 'X' else 'B'
        if board[0][0] == board[1][1] == board[2][2] != '':
            return 'A' if board[1][1] == 'X' else 'B'
        if board[0][2] == board[1][1] == board[2][0] != '':
            return 'A' if board[1][1] == 'X' else 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'