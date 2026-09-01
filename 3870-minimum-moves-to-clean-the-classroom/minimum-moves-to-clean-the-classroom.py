from typing import List
from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start = None
        litter = {}
        idx = 0
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter[(r, c)] = idx
                    idx += 1
        k = len(litter)
        if k == 0:
            return 0
        full_mask = (1 << k) - 1
        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]
        sr, sc = start
        best[sr][sc][0] = energy
        q = deque([(sr, sc, energy, 0)])
        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    ne = e - 1
                    if ne < 0:
                        continue
                    nmask = mask
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]
                    if classroom[nr][nc] == 'R':
                        ne = energy
                    if nmask == full_mask:
                        return moves + 1
                    if ne <= best[nr][nc][nmask]:
                        continue
                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, ne, nmask))
            moves += 1
        return -1