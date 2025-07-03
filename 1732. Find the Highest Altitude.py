class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = height = 0
        for g in gain:
            height += g
            if height > highest:
                highest = height
        return highest