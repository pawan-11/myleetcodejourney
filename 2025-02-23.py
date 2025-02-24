class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        ans = ""
        while i < len(s):
            ans += s[i:i+k][::-1]
            ans += s[i+k:i+2*k]
            i+=2*k
        return ans