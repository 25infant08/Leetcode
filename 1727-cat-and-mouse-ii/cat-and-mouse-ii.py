from typing import List
from collections import deque
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        R, C = len(grid), len(grid[0])
        N = R * C
        mouse = cat = food = 0
        for i in range(R):
            for j in range(C):
                p = i * C + j
                if grid[i][j] == 'M':
                    mouse = p
                elif grid[i][j] == 'C':
                    cat = p
                elif grid[i][j] == 'F':
                    food = p
        def moves(p, jump):
            x, y = divmod(p, C)
            res = [p]
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                for k in range(1, jump + 1):
                    nx, ny = x + dx * k, y + dy * k
                    if not (0 <= nx < R and 0 <= ny < C) or grid[nx][ny] == '#':
                        break
                    res.append(nx * C + ny)
            return res
        mm = [moves(i, mouseJump) for i in range(N)]
        cm = [moves(i, catJump) for i in range(N)]
        mp = [[] for _ in range(N)]
        cp = [[] for _ in range(N)]
        for i in range(N):
            for j in mm[i]:
                mp[j].append(i)
            for j in cm[i]:
                cp[j].append(i)
        state = bytearray(N * N * 2)
        degree = bytearray(N * N * 2)
        q = deque()
        def idx(m, c, t):
            return (m * N + c) * 2 + t
        for m in range(N):
            for c in range(N):
                degree[idx(m, c, 0)] = len(mm[m])
                degree[idx(m, c, 1)] = len(cm[c])
        for i in range(N):
            if i != food:
                for t in (0, 1):
                    state[idx(food, i, t)] = 1
                    state[idx(i, food, t)] = 2
                    state[idx(i, i, t)] = 2
                    q.append((food, i, t))
                    q.append((i, food, t))
                    q.append((i, i, t))
        while q:
            m, c, turn = q.popleft()
            winner = state[idx(m, c, turn)]
            if turn == 0:
                for pc in cp[c]:
                    k = idx(m, pc, 1)
                    if state[k]:
                        continue
                    if winner == 2:
                        state[k] = 2
                        q.append((m, pc, 1))
                    else:
                        degree[k] -= 1
                        if degree[k] == 0:
                            state[k] = 1
                            q.append((m, pc, 1))
            else:
                for pm in mp[m]:
                    k = idx(pm, c, 0)
                    if state[k]:
                        continue
                    if winner == 1:
                        state[k] = 1
                        q.append((pm, c, 0))
                    else:
                        degree[k] -= 1
                        if degree[k] == 0:
                            state[k] = 2
                            q.append((pm, c, 0))
        return state[idx(mouse, cat, 0)] == 1