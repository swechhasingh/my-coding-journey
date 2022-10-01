class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]: # discard right half and search in left half
                end = mid - 1
            elif target > nums[mid]: # discard left half and search in right half
                start = mid + 1
                
        return -1
    
                