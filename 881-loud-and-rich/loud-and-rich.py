class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a,b in richer:
            graph[b].append(a)
        n = len(quiet)
        answer = [-1] * n
        def dfs(i):
            if answer[i] != -1:
                return answer[i]
            answer[i] = i
            for nei in graph[i]:
                item = dfs(nei)
                if quiet[item] < quiet[answer[i]]:
                    answer[i] = item
            return answer[i]
        for i in range(n):
            val = dfs(i)
        return answer