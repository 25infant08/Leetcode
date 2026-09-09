import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 1
        self.heap = []
        self.seen = set()
    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.seen.remove(num)
            return num
        num = self.curr
        self.curr += 1
        return num
    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)