class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i , j = 0, 0
        start, end = 0, 1
        interval_intersection = []
        while i < len(firstList) and j < len(secondList):
            # a's start lies in b
            a_overlap_b = (firstList[i][start]>=secondList[j][start]) and (firstList[i][start]<=secondList[j][end])
            
            # b's start lies in a
            b_overlap_a = (firstList[i][start]<=secondList[j][start]) and (firstList[i][end]>=secondList[j][start]) 
            
            if a_overlap_b or b_overlap_a:
                merged_interval = [max(firstList[i][start], secondList[j][start]), min(firstList[i][end], secondList[j][end])]
                interval_intersection.append(merged_interval)
                
            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1
        return interval_intersection
                