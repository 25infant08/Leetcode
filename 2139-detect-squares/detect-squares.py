from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)
    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for (x2, y2), freq in self.points.items():
            if y2 != y or x2 == x:
                continue
            d = abs(x2 - x)
            result += freq * self.points.get((x, y + d), 0) * self.points.get((x2, y + d), 0)
            result += freq * self.points.get((x, y - d), 0) * self.points.get((x2, y - d), 0)
        return result