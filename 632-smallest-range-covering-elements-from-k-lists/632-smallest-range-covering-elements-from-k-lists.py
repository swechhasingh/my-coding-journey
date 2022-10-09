class Solution:
    # from heapq import *
    # import math
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        curr_largest_num = 0
        smallest_range = [-math.inf, math.inf]
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 1))
            curr_largest_num = max(curr_largest_num, nums[i][0])
        
        while min_heap:
            curr_min, curr_list, next_idx = heapq.heappop(min_heap)
            curr_range = [curr_min, curr_largest_num]
            
            # update smaller range
            if (curr_largest_num-curr_min) < (smallest_range[1]-smallest_range[0]):
                smallest_range = curr_range
            elif (curr_largest_num-curr_min) == (smallest_range[1]-smallest_range[0]) and curr_min < smallest_range[0]:
                smallest_range = curr_range
                
            if next_idx < len(nums[curr_list]):
                heapq.heappush(min_heap, (nums[curr_list][next_idx], curr_list, next_idx + 1))
                curr_largest_num = max(curr_largest_num, nums[curr_list][next_idx])
            else:
                break
        return smallest_range