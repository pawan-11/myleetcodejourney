class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        totalsm = sum(nums)
        if totalsm%2 != 0:
            return False
        
        def include(idx, subsetsm=0, subset=[]):
            #to include nums[idx] or to not, in subset, such that the leftover sum can be equal
            if subsetsm == totalsm-subsetsm:
                    return True
            #print(subsetsm, totalsm-subsetsm, subset)
            if idx == len(nums) or nums[idx]+subsetsm > totalsm-subsetsm-nums[idx]:
                return False

            return include(idx+1, subsetsm+nums[idx], subset+[nums[idx]]) \
            or include(idx+1, subsetsm, subset) #not include
                
        x = include(0)
        return x