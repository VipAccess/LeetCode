class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2:
                ans.append(1)
            else:
                ans.insert(0, 0)
        return ans