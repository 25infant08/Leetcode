class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            x = mountainArr.get(m)
            if x == target:
                return m
            elif x < target:
                l = m + 1
            else:
                r = m - 1
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            x = mountainArr.get(m)
            if x == target:
                return m
            elif x > target:
                l = m + 1
            else:
                r = m - 1
        return -1