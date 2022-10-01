class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # when input list is empty
        
        right_end = self.findLimit(nums, target, True)
        if right_end == -1:
            return [-1,-1]
        left_end = self.findLimit(nums, target, False)
        if left_end == -1:
            return [-1,-1]
        return [left_end, right_end]
    
    def findLimit(self, nums, target, upper_limit):
        
        start = 0
        end = len(nums)-1
        keyIndex = -1
        while start <= end:
            mid = (start + end)//2
    
            if target < nums[mid]: # discard right half and search in left half
                end = mid-1
            elif target > nums[mid]: # discard left half and search in right half
                start = mid + 1
            else:
                keyIndex = mid
                if upper_limit:
                    start = mid + 1
                else:
                    end = mid - 1
        return keyIndex
    