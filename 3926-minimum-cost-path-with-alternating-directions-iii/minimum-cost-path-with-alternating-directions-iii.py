class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        def actions(i, j, p):
            for di, dj in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    fee = (ii + 1) * (jj + 1) if di or dj else 0
                    yield fee + (di + dj != p) * penalty[i][j], (ii, jj, -p)
        pq = [(1, (0, 0, 1))]
        seen = set()
        while pq:
            d, s = heappop(pq)
            if s in seen:
                continue
            seen.add(s)
            i, j, p = s
            if (i, j) == (m - 1, n - 1):
                return d
            for w, t in actions(i, j, p):
                if t not in seen:
                    heappush(pq, (d + w, t))