from collections import deque
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = deque()
        self.total = 0
        self.n = 100001
        self.count = [0] * (self.n + 1)
        self.sum = [0] * (self.n + 1)
    def update(self, bit, i, delta):
        while i <= self.n:
            bit[i] += delta
            i += i & -i
    def query(self, bit, i):
        res = 0
        while i:
            res += bit[i]
            i -= i & -i
        return res
    def kth(self, k):
        idx = 0
        bit_mask = 1 << 17
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.count[nxt] < k:
                idx = nxt
                k -= self.count[nxt]
            bit_mask >>= 1
        return idx + 1
    def sum_smallest(self, k):
        if k == 0:
            return 0
        x = self.kth(k)
        cnt_before = self.query(self.count, x - 1)
        sum_before = self.query(self.sum, x - 1)
        return sum_before + (k - cnt_before) * x
    def addElement(self, num: int) -> None:
        self.q.append(num)
        self.total += num
        self.update(self.count, num, 1)
        self.update(self.sum, num, num)
        if len(self.q) > self.m:
            old = self.q.popleft()
            self.total -= old
            self.update(self.count, old, -1)
            self.update(self.sum, old, -old)
    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        small = self.sum_smallest(self.k)
        small_and_middle = self.sum_smallest(self.m - self.k)
        large = self.total - small_and_middle
        middle = self.total - small - large
        return middle // (self.m - 2 * self.k)