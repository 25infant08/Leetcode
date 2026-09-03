class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = [0] * n
        for i, x in enumerate(nums2):
            pos[x] = i
        arr = [pos[x] for x in nums1]
        def update(bit, i):
            while i <= n:
                bit[i] += 1
                i += i & -i
        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s
        left = [0] * n
        bit = [0] * (n + 1)
        for i in range(n):
            x = arr[i] + 1
            left[i] = query(bit, x - 1)
            update(bit, x)
        right = [0] * n
        bit = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = arr[i] + 1
            right[i] = query(bit, n) - query(bit, x)
            update(bit, x)
        return sum(left[i] * right[i] for i in range(n))