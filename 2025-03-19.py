class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        i = 0
        while i < len(nums)-2:
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                flips += 1
            i+=1
        return flips if nums[-1] == nums[-2] == 1 else -1