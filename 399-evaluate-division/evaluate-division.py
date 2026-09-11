class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (a, b), value in zip(equations, values):
            graph.setdefault(a, []).append((b, value))
            graph.setdefault(b, []).append((a, 1 / value))
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        result = []
        for a, b in queries:
            result.append(dfs(a, b, set()))
        return result