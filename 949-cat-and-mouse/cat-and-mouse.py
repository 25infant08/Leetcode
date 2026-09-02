from typing import List
from collections import deque
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        MOUSE = 0
        CAT = 1
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        color = [
            [
                [DRAW] * 2
                for _ in range(n)
            ]
            for _ in range(n)
        ]
        degree = [
            [
                [0] * 2
                for _ in range(n)
            ]
            for _ in range(n)
        ]
        for mouse in range(n):
            for cat in range(n):
                degree[mouse][cat][MOUSE] = len(graph[mouse])
                degree[mouse][cat][CAT] = sum(
                    next_node != 0
                    for next_node in graph[cat]
                )
        queue = deque()
        for cat in range(1, n):
            color[0][cat][MOUSE] = MOUSE_WIN
            color[0][cat][CAT] = MOUSE_WIN
            queue.append((0, cat, MOUSE))
            queue.append((0, cat, CAT))
        for node in range(1, n):
            color[node][node][MOUSE] = CAT_WIN
            color[node][node][CAT] = CAT_WIN
            queue.append((node, node, MOUSE))
            queue.append((node, node, CAT))
        while queue:
            mouse, cat, turn = queue.popleft()
            result = color[mouse][cat][turn]
            if turn == MOUSE:
                for previous_cat in graph[cat]:
                    if previous_cat == 0:
                        continue
                    prev_state = color[mouse][previous_cat][CAT]
                    if prev_state != DRAW:
                        continue
                    if result == CAT_WIN:
                        color[mouse][previous_cat][CAT] = CAT_WIN
                        queue.append(
                            (mouse, previous_cat, CAT)
                        )
                    else:
                        degree[mouse][previous_cat][CAT] -= 1
                        if degree[mouse][previous_cat][CAT] == 0:
                            color[mouse][previous_cat][CAT] = MOUSE_WIN
                            queue.append(
                                (mouse, previous_cat, CAT)
                            )
            else:
                for previous_mouse in graph[mouse]:
                    prev_state = color[previous_mouse][cat][MOUSE]
                    if prev_state != DRAW:
                        continue
                    if result == MOUSE_WIN:
                        color[previous_mouse][cat][MOUSE] = MOUSE_WIN
                        queue.append(
                            (previous_mouse, cat, MOUSE)
                        )
                    else:
                        degree[previous_mouse][cat][MOUSE] -= 1
                        if degree[previous_mouse][cat][MOUSE] == 0:
                            color[previous_mouse][cat][MOUSE] = CAT_WIN
                            queue.append(
                                (previous_mouse, cat, MOUSE)
                            )
        return color[1][2][MOUSE]