from typing import List
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(instructions)
        MAX = 100000
        bit = [0] * (MAX + 1)
        def update(i: int):
            while i <= MAX:
                bit[i] += 1
                i += i & -i
        def query(i: int) -> int:
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total
        ans = 0
        for i, x in enumerate(instructions):
            less = query(x - 1)
            less_or_equal = query(x)
            greater = i - less_or_equal
            ans = (ans + min(less, greater)) % MOD
            update(x)
        return ans