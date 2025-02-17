class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        i = 0
        while i < len(s):
            count = 0
            char = s[i]
            while i < len(s) and s[i] == char:
                count += 1
                i += 1
            if count == k:
                return True
        return False