class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        curr = 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1