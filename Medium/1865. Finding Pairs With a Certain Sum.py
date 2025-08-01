from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]

        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        result = 0
        for x in self.freq1:
            if (tot - x) in self.freq2:
                result += self.freq1[x] * self.freq2[tot - x]
        return result

    # Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)