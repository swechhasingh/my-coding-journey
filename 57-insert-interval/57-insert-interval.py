class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        i = 0
        start, end = 0, 1
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            new_intervals.append(intervals[i])
            i += 1
            
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
        new_intervals.append(newInterval)
                
        while i < len(intervals):
            new_intervals.append(intervals[i])
            i += 1
        return new_intervals