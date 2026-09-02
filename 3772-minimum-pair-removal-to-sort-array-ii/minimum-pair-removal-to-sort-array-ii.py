from typing import List
import heapq
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        a = nums[:]
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]
        nxt[-1] = -1
        alive = [True] * n
        version = [0] * n
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (a[i] + a[i + 1], i, version[i]))
        bad = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                bad += 1
        ans = 0
        while bad > 0:
            while True:
                s, i, v = heapq.heappop(heap)
                if not alive[i]:
                    continue
                j = nxt[i]
                if j == -1 or not alive[j]:
                    continue
                if version[i] != v:
                    continue
                if a[i] + a[j] != s:
                    continue
                break
            j = nxt[i]
            p = prev[i]
            q = nxt[j]
            if p != -1 and a[p] > a[i]:
                bad -= 1
            if a[i] > a[j]:
                bad -= 1
            if q != -1 and a[j] > a[q]:
                bad -= 1
            a[i] += a[j]
            alive[j] = False
            nxt[i] = q
            if q != -1:
                prev[q] = i
            version[i] += 1
            version[j] += 1
            if p != -1:
                version[p] += 1
                if a[p] > a[i]:
                    bad += 1
                heapq.heappush(
                    heap,
                    (a[p] + a[i], p, version[p])
                )
            if q != -1:
                if a[i] > a[q]:
                    bad += 1
                heapq.heappush(
                    heap,
                    (a[i] + a[q], i, version[i])
                )
            ans += 1
        return ans