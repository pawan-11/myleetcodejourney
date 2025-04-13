class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        toprow = [1 for i in range(m)]
        currrow = toprow
        for row in range(1,n):
            currrow = [toprow[0]]
            for j in range(1,m):
                currrow.append(currrow[-1]+toprow[j])
            toprow = currrow
        
        return currrow[-1]