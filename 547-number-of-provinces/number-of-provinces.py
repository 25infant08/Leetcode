class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(n):
            if i in visited:
                continue
            provinces += 1
            stack = [i]
            while stack:
                city = stack.pop()
                if city in visited:
                    continue
                visited.add(city)
                for j in range(n):
                    if isConnected[city][j] == 1 and j not in visited:
                        stack.append(j)
        return provinces