class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][n - 1] == "O":
                stack.append((i, n - 1))
        for j in range(n):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[m - 1][j] == "O":
                stack.append((m - 1, j))
        while stack:
            i, j = stack.pop()
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                continue
            board[i][j] = "#"
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"