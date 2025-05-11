class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for i in arr:
            if i% 2:
                odds+=1
                if odds == 3:
                    return True
            else:
                odds = 0
        return odds == 3