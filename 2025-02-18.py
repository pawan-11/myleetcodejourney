class Solution:
    def findValidPair(self, s: str) -> str:
        c = Counter(s)
        #items = list(c.items())
        i = 1
        while i < len(s):
            if (s[i] != s[i-1] and c[s[i]] == int(s[i]) 
            and c[s[i-1]] == int(s[i-1])):
                return s[i-1]+s[i]
            i+=1
        return ""