class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix[0])
        n = len(matrix)

        r = m*n-1

        while l> -1 and r < m*n and l <= r:
            mid= (l+r)//2
            ro, co= mid//m, mid%m
            #print(l, r)
            if l == r:
                return  matrix[ro][co] == target
            if matrix[ro][co] == target:
                return True
            elif matrix[ro][co] < target:
                l = mid+1
            else:
                r = mid-1

        return False
            