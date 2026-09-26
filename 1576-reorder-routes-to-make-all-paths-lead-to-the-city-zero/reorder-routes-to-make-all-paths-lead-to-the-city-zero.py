class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        visited = set()
        stack = [0]
        result = 0
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for nei, cost in graph[node]:
                if nei not in visited:
                    result += cost
                    stack.append(nei)
        return result