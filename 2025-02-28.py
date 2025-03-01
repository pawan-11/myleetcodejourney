class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
            if nums[i-1] != 0:
                res.append(nums[i-1])
        if nums[-1] != 0:
            res.append(nums[-1])
        for i in range(len(nums)-len(res)):
            res.append(0)
        return res