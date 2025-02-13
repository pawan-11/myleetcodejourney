import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0
        while len(nums)>1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k:
                break
            heapq.heappush(nums, min(x,y)*2+max(x,y))
            op+=1
        return op