class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        quads = []
        #3 pointers

        i = 0
        j = 1 
        while i < len(nums)-3:
            j = i + 1
            while j < len(nums)-2:
                k = j+1 #increase this to increase sum
                l = len(nums)-1 #decrease this to decrease sum
                
                while k < l:
                    #print(nums[i],nums[j],nums[k],nums[l])
                    sm = nums[i]+nums[j]+nums[k]+nums[l]
                    if sm == target:
                        quads.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                    elif sm < target:
                        k += 1
                    elif sm > target:
                        l -= 1
                j += 1
                while j < len(nums)-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < len(nums)-3 and nums[i] == nums[i-1]:
                i += 1
        return quads