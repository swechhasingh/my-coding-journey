class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        inversion_pt = -1
        # find the inversion point: move from right to left and find where the ascending order breaks
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                inversion_pt = i
                break
        # if inversion point exists, find the next largest number to nums[inversion_pt] in the array after the inversion_pt
        if inversion_pt >= 0:
            j = inversion_pt + 1
            while j < len(nums)  and nums[j] > nums[inversion_pt]:
                j += 1
                
            # swap the inversion_pt and it's next largest number
            nums[inversion_pt], nums[j-1] = nums[j-1], nums[inversion_pt]
        
        # reverse the part of array starting from inversion_pt + 1 (i.e sort it in ascending order)
        i = inversion_pt + 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
            