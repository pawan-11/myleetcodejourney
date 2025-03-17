class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for e,v in c.items():
            if v%2 != 0:
                return False
        return True