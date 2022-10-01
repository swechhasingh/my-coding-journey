class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        key_range = [-1,-1]
        key_range[1] = self.findLimit(nums, target, True)
        if key_range[1] != -1:
            key_range[0] = self.findLimit(nums, target, False)
        return key_range
    
    def findLimit(self, nums, target, upper_limit):
        start = 0
        end = len(nums)-1
        # targetIndex will keep track of target's last seen index
        targetIndex = -1
        while start <= end:
            mid = (start + end)//2
            if target < nums[mid]: # discard right half and search in left half
                end = mid-1
            elif target > nums[mid]: # discard left half and search in right half
                start = mid + 1
            else:
                targetIndex = mid  # keep track of target's last seen index
                if upper_limit:
                    start = mid + 1 # keep looking on right handside for RHL of the range
                else:
                    end = mid - 1 # keep looking on left handside for LHL of the range
        return targetIndex
    