class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        # sort the intervals on start
        intervals.sort(key=lambda x: x[0])
        
        start, end = 0, 1
        merged_interval = intervals[0]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            if curr_interval[start] <= merged_interval[end]:
                merged_interval[end] = max(merged_interval[end], curr_interval[end])
            else:
                merged_intervals.append(merged_interval)
                merged_interval = curr_interval
        merged_intervals.append(merged_interval)
        return merged_intervals
        
        