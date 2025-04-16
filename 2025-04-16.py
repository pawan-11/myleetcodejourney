class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        indexes = {}
        pairs = {} #good pairs for each number that there are 2 of in array
        acc = []
        goodpairs = 0
        for i,num in enumerate(nums):
            if indexes.get(num):
                pairs[num] += indexes[num]
                goodpairs += indexes[num]
                indexes[num] += 1
            else:
                indexes[num] = 1
                pairs[num] = 0
            acc.append(goodpairs)
        print(pairs, acc)

        #2 pointer on acc to find number of subarrays that have at least k good pairs
        #acc is sorted
        j = len(acc)-1
        i = 0
        goodarrs = 0
        
        while i < j:
            j = len(acc)-1
            while j > i:
                if acc[j]-acc[i] >=k:
                    print(nums[i:j+1]," is good")
                    goodarrs+=1
                else:
                    break     
                j -= 1
            i += 1
        return goodarrs
        
