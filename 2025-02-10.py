class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        while i < len(s):
            j = 0
            while i+j < len(s) and j < len(part) and s[i+j] == part[j]:
                j+=1
            if j != len(part):
                i+=1
            else:
                s = s[:i]+s[i+j:]
                i = max(0, i-len(part))
        return s