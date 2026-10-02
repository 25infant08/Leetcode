class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        has_incoming = [False] * n
        for a, b in edges:
            has_incoming[b] = True
        return [i for i in range(n) if not has_incoming[i]]