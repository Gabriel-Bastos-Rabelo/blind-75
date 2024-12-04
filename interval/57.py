#first solution
#time complexity O(nlogn)
#space complexity O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= interval[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res
          


#second sulution
#time complexity O(n)
#space complexity O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []

        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1 

        res.append(newInterval)
        res.extend(intervals[i:])
        
        return res


          
