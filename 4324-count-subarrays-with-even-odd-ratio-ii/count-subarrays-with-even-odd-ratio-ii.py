class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x % 2 == 0:
                prefix[i + 1] = prefix[i] + b
            else:
                prefix[i + 1] = prefix[i] - a
        def merge_sort(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)
            j = mid
            for i in range(left, mid):
                while j < right and prefix[j] <= prefix[i]:
                    j += 1
                count += j - mid
            temp = []
            i, j = left, mid
            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    temp.append(prefix[i])
                    i += 1
                else:
                    temp.append(prefix[j])
                    j += 1
            while i < mid:
                temp.append(prefix[i])
                i += 1
            while j < right:
                temp.append(prefix[j])
                j += 1
            prefix[left:right] = temp
            return count
        return merge_sort(0, n + 1)