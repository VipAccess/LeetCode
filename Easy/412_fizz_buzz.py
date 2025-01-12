class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for digit in range(1, n + 1):
            if not (digit % 3 == 0) and not (digit % 5 == 0):
                result.append(str(digit))
            elif digit % 15 == 0:
                result.append('FizzBuzz')
            elif digit % 3 == 0:
                result.append('Fizz')
            else:
                result.append('Buzz')
        return result