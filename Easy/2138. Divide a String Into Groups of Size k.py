class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s += fill * (-len(s) % k)
        ans = []
        for i in range(0, len(s), k):
            print(s[i: i + k])
            ans.append(s[i: i + k])
        return ans