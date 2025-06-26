class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for el in hours:
            if el >= target:
                ans += 1
        return ans