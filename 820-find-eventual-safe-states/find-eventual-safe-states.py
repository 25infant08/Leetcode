class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        deg = [0] * len(graph)
        rev = [[] for _ in range(len(graph))]
        for u in range(len(graph)):
            deg[u] = len(graph[u])
            for v in graph[u]:
                rev[v].append(u)
        q = deque()
        op = []
        for i in range(len(graph)):
            if deg[i] == 0:
                q.append(i)
        while q:
            n = q.popleft()
            op.append(n)
            for i in rev[n]:
                deg[i] -= 1
                if deg[i] == 0:
                    q.append(i)
        return sorted(op)