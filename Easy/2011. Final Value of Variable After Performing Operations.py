class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for el in operations:
            if '-' in el:
                ans -= 1
            else:
                ans += 1
        return ans