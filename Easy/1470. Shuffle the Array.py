class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans += [nums[i]]
            ans += [nums[i+n]]
        return ans