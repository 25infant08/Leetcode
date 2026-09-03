class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]
        def merge_sort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid)
            count += merge_sort(mid + 1, right)
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and arr[j] < arr[i] - diff:
                    j += 1
                count += right - j + 1
            temp = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            arr[left:right + 1] = temp
            return count
        return merge_sort(0, len(arr) - 1)