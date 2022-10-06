class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height)-1
        max_area = 0
        while left < right:
            if height[left] <= height[right]:
                min_height = height[left]
                area = (right -left)*min_height
                left += 1
            else:
                min_height = height[right]
                area = (right -left)*min_height
                right -= 1
            max_area = max(max_area, area)
        return max_area