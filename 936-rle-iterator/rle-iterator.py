from typing import List
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0
    def next(self, n: int) -> int:
        while self.i < len(self.encoding):
            count = self.encoding[self.i]
            value = self.encoding[self.i + 1]
            if n > count:
                n -= count
                self.encoding[self.i] = 0
                self.i += 2
            else:
                self.encoding[self.i] -= n
                return value
        return -1