class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            if wealth > total:
                total = wealth
        return total