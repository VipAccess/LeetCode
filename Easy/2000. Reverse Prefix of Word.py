class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        if ch in word:
            idx = word.index(ch)
        return word[idx::-1] + word[idx+1:]