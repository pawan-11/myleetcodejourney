class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        i = 1
        prevend = -1
        
        while i < len(intervals):
            start, end = intervals[i]
            if start > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], end)
            i+=1
        return ans