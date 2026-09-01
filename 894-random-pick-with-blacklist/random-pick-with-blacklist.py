import random
from typing import List
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.m = n - len(blacklist)
        self.mapping = {}
        blacklist_set = set(blacklist)
        last = n - 1
        for b in blacklist:
            if b < self.m:
                while last in blacklist_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1
    def pick(self) -> int:
        x = random.randrange(self.m)
        if x in self.mapping:
            return self.mapping[x]
        return x