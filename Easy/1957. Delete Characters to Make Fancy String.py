class Solution:
    def makeFancyString(self, s: str) -> str:
        for char in set(s):
            while char * 3 in s:
                s = s.replace(char * 3, char * 2)
        return s
