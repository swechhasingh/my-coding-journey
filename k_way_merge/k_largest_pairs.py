import heapq

def find_k_largest_pairs(list1, list2, k):
    min_heap = []
    
    for i in range(min(k, len(list1))):
        for j in range(min(k, len(list2))):
            curr_sum = list1[i] + list2[j]
            if len(min_heap) < k:
                heapq.heappush(min_heap, (curr_sum, [list1[i], list2[j]]))
            else:
                if min_heap[0][0] > curr_sum:
                    break
                else:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (curr_sum, [list1[i], list2[j]]))
            
    return [element[1] for element in min_heap]

def main():
    print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()