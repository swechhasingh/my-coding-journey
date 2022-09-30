class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target > letters[-1]:
            return letters[0]
        if target < letters[0]:
            return letters[0]
        start = 0
        end = len(letters)-1
        
        while start <= end:
            mid = (start + end)//2
            
            if mid > 0 and letters[mid-1] <= target and target < letters[mid]:
                return letters[mid]
            
            if mid < len(letters)-1 and letters[mid+1] > target and target >= letters[mid]:
                return letters[mid + 1]
            
            if target < letters[mid]: # discard right half and search in left half
                end = mid
            elif target >= letters[mid]: # discard left half and search in right half
                start = mid + 1
                
        return letters[0]