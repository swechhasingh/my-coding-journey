import heapq

def find_Kth_smallest(matrix, k):
    row = len(matrix)
    col = len(matrix[0])

    min_heap = []
    for r in range(min(k,row)):
        heapq.heappush(min_heap, (matrix[r][0], r, 0))
    
    count_num = 0
    while min_heap:
        curr_min_num, row, row_idx = heapq.heappop(min_heap)
        count_num += 1
        if count_num == k:
            return curr_min_num
        if row_idx + 1 < col:
            heapq.heappush(min_heap, (matrix[row][row_idx + 1], row, row_idx + 1))
    return -1



def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()