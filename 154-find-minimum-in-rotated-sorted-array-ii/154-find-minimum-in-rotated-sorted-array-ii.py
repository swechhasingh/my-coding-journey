class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums)-1
        while start < end:
            mid = (start+end)//2
            
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[start] == nums[end] and nums[start] == nums[mid]:
                end -= 1
                start += 1
            elif nums[start] < nums[end]:
                end = mid - 1
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid
        return nums[start]