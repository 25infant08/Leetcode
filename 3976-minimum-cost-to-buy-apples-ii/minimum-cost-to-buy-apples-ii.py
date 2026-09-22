class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        emptyGraph = [[] for _ in range(n)]
        carryGraph = [[] for _ in range(n)]
        for u, v, cost, taxi in roads:
            emptyGraph[u].append((v, cost))
            emptyGraph[v].append((u, cost))
            carry_cost = cost * taxi
            carryGraph[u].append((v, carry_cost))
            carryGraph[v].append((u, carry_cost))
        INF = 10**18
        ans = [0] * n
        emptyDist = [INF] * n
        carryDist = [INF] * n
        for src in range(n):
            for i in range(n):
                emptyDist[i] = INF
            emptyDist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > emptyDist[u]:
                    continue
                for v, w in emptyGraph[u]:
                    if emptyDist[v] > d + w:
                        emptyDist[v] = d + w
                        heapq.heappush(
                            pq,
                            (emptyDist[v], v)
                        )
            for i in range(n):
                carryDist[i] = INF
            carryDist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > carryDist[u]:
                    continue
                for v, w in carryGraph[u]:
                    if carryDist[v] > d + w:
                        carryDist[v] = d + w
                        heapq.heappush(
                            pq,
                            (carryDist[v], v)
                        )
            best = prices[src]
            for shop in range(n):
                if (emptyDist[shop] == INF or
                    carryDist[shop] == INF):
                    continue
                total = (
                    emptyDist[shop]
                    + carryDist[shop]
                    + prices[shop]
                )
                best = min(best, total)
            ans[src] = best
        return ans