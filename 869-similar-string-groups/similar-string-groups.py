class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                parent[b] = a
        def similar(a, b):
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                if diff > 2:
                    return False
            return True
        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]) and find(i) != find(j):
                    union(i, j)
                    groups -= 1
        return groups