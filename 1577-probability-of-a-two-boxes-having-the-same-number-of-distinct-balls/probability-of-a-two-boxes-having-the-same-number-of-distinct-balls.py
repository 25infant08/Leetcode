class Solution:
    def getProbability(self, balls: List[int]) -> float:
        from math import comb
        n = sum(balls) // 2
        total = 0
        good = 0
        def dfs(i, box1, box2, distinct1, distinct2, ways):
            nonlocal total, good
            if i == len(balls):
                if box1 == n and box2 == n:
                    total += ways
                    if distinct1 == distinct2:
                        good += ways
                return
            count = balls[i]
            for x in range(count + 1):
                y = count - x
                if box1 + x > n or box2 + y > n:
                    continue
                new_distinct1 = distinct1 + (x > 0)
                new_distinct2 = distinct2 + (y > 0)
                dfs(
                    i + 1,
                    box1 + x,
                    box2 + y,
                    new_distinct1,
                    new_distinct2,
                    ways * comb(count, x)
                )
        dfs(0, 0, 0, 0, 0, 1)
        return good / total