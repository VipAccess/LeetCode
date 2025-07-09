class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        num2 = num
        while num2:
            if num % (num2 % 10) == 0:
                ans += 1
            num2 //= 10
        return ans