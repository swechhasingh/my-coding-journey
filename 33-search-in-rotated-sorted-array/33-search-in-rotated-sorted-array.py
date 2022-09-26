class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            # print(left,right)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # left part is sorted
                if target < nums[mid] and target >= nums[left]: 
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right part is sorted
                if target > nums[mid] and target <= nums[right]: 
                    left = mid + 1
                else:
                    right = mid - 1
                   
        return -1
        