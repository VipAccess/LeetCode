class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        position = 0
        for num in nums:
            if num >= target:
                return position
            position += 1
        return position