class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inversion_pt = -1
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
        n = len(nums)
        j = 1
        while i < (n-j):
            nums[i], nums[n-j] = nums[n-j], nums[i]
            i += 1
            j += 1
        return nums
            