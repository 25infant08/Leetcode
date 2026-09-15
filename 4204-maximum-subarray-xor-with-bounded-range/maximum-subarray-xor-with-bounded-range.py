from typing import List
from collections import deque
class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] ^ x
        left_child = [0]
        right_child = [0]
        count = [0]
        roots = [0]
        def insert(prev, x):
            root = len(count)
            left_child.append(left_child[prev])
            right_child.append(right_child[prev])
            count.append(count[prev] + 1)
            cur = root
            old = prev
            for bit in range(14, -1, -1):
                b = (x >> bit) & 1
                if b == 0:
                    nxt = left_child[old]
                    node = len(count)
                    left_child.append(left_child[nxt])
                    right_child.append(right_child[nxt])
                    count.append(count[nxt] + 1)
                    left_child[cur] = node
                else:
                    nxt = right_child[old]
                    node = len(count)
                    left_child.append(left_child[nxt])
                    right_child.append(right_child[nxt])
                    count.append(count[nxt] + 1)
                    right_child[cur] = node
                cur = node
                old = nxt
            return root
        for x in pre:
            roots.append(insert(roots[-1], x))
        def query(l, r, x):
            a = roots[l]
            b = roots[r + 1]
            ans = 0
            for bit in range(14, -1, -1):
                xb = (x >> bit) & 1
                if xb == 0:
                    na = right_child[a]
                    nb = right_child[b]
                else:
                    na = left_child[a]
                    nb = left_child[b]
                if count[nb] - count[na] > 0:
                    ans |= 1 << bit
                    a, b = na, nb
                else:
                    if xb == 0:
                        a = left_child[a]
                        b = left_child[b]
                    else:
                        a = right_child[a]
                        b = right_child[b]
            return ans
        mx = deque()
        mn = deque()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            while mx and nums[mx[-1]] <= x:
                mx.pop()
            mx.append(right)
            while mn and nums[mn[-1]] >= x:
                mn.pop()
            mn.append(right)
            while nums[mx[0]] - nums[mn[0]] > k:
                if mx[0] == left:
                    mx.popleft()
                if mn[0] == left:
                    mn.popleft()
                left += 1
            ans = max(ans, query(left, right, pre[right + 1]))
        return ans