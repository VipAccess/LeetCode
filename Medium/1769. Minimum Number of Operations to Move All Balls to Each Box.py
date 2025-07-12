class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        index_set = {i for i in range(len(boxes)) if boxes[i] == '1'}
        for i in range(len(boxes)):
            num = 0
            for el in index_set:
                num += abs(el - i)
            ans.append(num)
        return ans