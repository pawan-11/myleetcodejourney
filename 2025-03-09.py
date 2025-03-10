class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cum = [nums[0]]
        for i in range(1, len(nums)):
            cum.append(cum[i-1] + nums[i])
        even = 0
        for i in range(0, len(nums)-1):
            if (cum[-1]-2*cum[i])%2 == 0:
                even+=1
        return even
