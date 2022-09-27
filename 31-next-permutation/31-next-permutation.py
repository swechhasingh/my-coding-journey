class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inversion_pt = -1
        # find the inversion point: move from right to left and find where the ascending order breaks
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                inversion_pt = i
                break
                
        if inversion_pt >= 0:
            j = inversion_pt + 1
            while j < len(nums)  and nums[j] > nums[inversion_pt]:
                j += 1
            nums[inversion_pt], nums[j-1] = nums[j-1], nums[inversion_pt]
            
        i = inversion_pt + 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
            