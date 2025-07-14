class Solution:
    def sortSentence(self, s: str) -> str:
        words = [(el[:-1], el[-1]) for el in s.split()]
        words.sort(key=lambda x: x[1])
        ans = [el[0] for el in words]
        return ' '.join(ans)