from bisect import insort
class SORTracker:
    def __init__(self):
        self.locations = []
        self.k = 0
    def add(self, name: str, score: int) -> None:
        insort(self.locations, (-score, name))
    def get(self) -> str:
        self.k += 1
        return self.locations[self.k - 1][1]