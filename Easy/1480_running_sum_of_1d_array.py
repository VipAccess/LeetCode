class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        term = nums[0]
        for i in range(1, len(nums)):
            nums[i] = term = nums[i] + term
        return nums
