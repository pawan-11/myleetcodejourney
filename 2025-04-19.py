class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        fairpairs = 0
        print(nums)
        while i < j:
            print(i, j, nums[i], nums[j])
            sm = nums[i]+nums[j]
            if sm < lower:
                i += 1
            elif sm > upper:
                j -= 1
            else:
                fairpairs += j-i
                i += 1
        return fairpairs