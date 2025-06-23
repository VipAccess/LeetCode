class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candies = max(candies)
        for kid in candies:
            if kid + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans