from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            pa, ca = a
            pb, cb = b
            p = pa * pb % k
            c = ca[:]
            for r in range(k):
                c[pa * r % k] += cb[r]
            return p, c
        size = 1
        while size < n:
            size <<= 1
        tree = [None] * (2 * size)
        for i, v in enumerate(nums):
            r = v % k
            c = [0] * k
            c[r] = 1
            tree[size + i] = (r, c)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])
        def update(pos, val):
            i = size + pos
            r = val % k
            c = [0] * k
            c[r] = 1
            tree[i] = (r, c)
            i >>= 1
            while i:
                tree[i] = merge(tree[i << 1], tree[i << 1 | 1])
                i >>= 1
        def query(l, r):
            left = right = None
            l += size
            r += size
            while l < r:
                if l & 1:
                    left = merge(left, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    right = merge(tree[r], right)
                l >>= 1
                r >>= 1
            return merge(left, right)
        ans = []
        for index, value, start, x in queries:
            update(index, value)
            ans.append(query(start, n)[1][x])
        return ans