class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        goal = len(set(nums))
        ans = 0
        while in range(len(nums)):
            curr = set()
            for j in range(i, len(nums)):
                curr.add(nums[j])
                if len(curr) == len(goal):
                    ans += 1
        return ans