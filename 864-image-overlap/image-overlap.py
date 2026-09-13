from typing import List
from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = []
        ones2 = []
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    ones1.append((r, c))
                if img2[r][c]:
                    ones2.append((r, c))
        count = defaultdict(int)
        ans = 0
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                count[shift] += 1
                ans = max(ans, count[shift])
        return ans