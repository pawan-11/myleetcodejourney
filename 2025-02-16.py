class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            if (i-k < 0 or nums[i-k] < nums[i]) and (i+k >= len(nums) or nums[i+k] < nums[i]):
                ans += nums[i]
        return ans