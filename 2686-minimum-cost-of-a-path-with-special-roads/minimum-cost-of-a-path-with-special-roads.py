from typing import List
import heapq
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        n = len(specialRoads)
        dist = [10**18] * n
        pq = [(0, start[0], start[1])]
        ans = abs(start[0] - target[0]) + abs(start[1] - target[1])
        while pq:
            d, x, y = heapq.heappop(pq)
            if d > ans:
                continue
            ans = min(ans, d + abs(x - target[0]) + abs(y - target[1]))
            for i, (x1, y1, x2, y2, cost) in enumerate(specialRoads):
                nd = d + abs(x - x1) + abs(y - y1) + cost
                if nd < dist[i]:
                    dist[i] = nd
                    heapq.heappush(pq, (nd, x2, y2))
        return ans