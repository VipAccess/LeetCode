class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x: len(x))
        unique = set()
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    unique.add(words[i])
        return list(unique)
