#time complexity O(nlogn)
#space complexity o(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        print(intervals)
        last = intervals[0]  
        for i in range(1, len(intervals)):
            if intervals[i][0] < last[1]:
                ans += 1
            else:
                last = intervals[i]

        return ans