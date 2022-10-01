class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            
            if mid > 0 and nums[mid-1] < target and target < nums[mid]:
                return mid
            
            if mid < len(nums)-1 and nums[mid+1] > target and target > nums[mid]:
                return mid + 1
            
            if target < nums[mid]: # discard right half and search in left half
                end = mid - 1
            elif target > nums[mid]: # discard left half and search in right half
                start = mid + 1
                
        return -1
    