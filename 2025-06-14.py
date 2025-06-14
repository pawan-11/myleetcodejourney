class Solution:
    def minMaxDifference(self, num: int) -> int:
        x = str(num)

        for i in range(len(x)):
            if x[i] != '9':
                mx = int(x[:i]+'9'+x[i+1:])
                break
        for i in range(len(x)-1,-1,-1):
            if x[i] != '0':
                mn = int(x[:i]+'0'+x[i+1:])
                break
        print(mn, mx)
        return mx - mn