class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        actual = 0
        for char in s:
            if char == '(':
                actual += 1
            elif char == ')':
                actual -= 1
            if actual > max_depth:
                max_depth = actual
        return max_depth