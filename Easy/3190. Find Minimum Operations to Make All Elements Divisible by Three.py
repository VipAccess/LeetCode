class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for n in nums:
            rest = n % 3
            if rest == 0:
                continue
            else:
                ops += 1

        return ops