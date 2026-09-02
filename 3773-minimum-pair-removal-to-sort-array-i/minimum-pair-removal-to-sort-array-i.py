class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while True:
            sorted_array = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_array = False
                    break
            if sorted_array:
                return operations
            min_sum = float('inf')
            index = 0
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i
            nums[index:index + 2] = [min_sum]
            operations += 1