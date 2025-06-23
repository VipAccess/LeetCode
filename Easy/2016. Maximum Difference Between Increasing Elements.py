class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    if diff > max_diff:
                        max_diff = diff
        return max_diff