class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        x = set()
        repeated = -1
        for i in grid:
            for j in i:
                if repeated == -1 and j in x:
                    repeated = j
                x.add(j)
        for i in range(1, len(grid)**2+1):
            if i not in x:
                return repeated, i
        