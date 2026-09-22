class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        heap, ans = [(0, 0)], [-1] * n
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))
        while heap:
            w1, node1 = heappop(heap)
            if ans[node1] != -1: continue
            ans[node1] = w1
            for w2, node2 in graph[node1]:
                w2+= w1
                if w2 >= disappear[node2]: continue
                heappush(heap, (w2, node2))
        return ans