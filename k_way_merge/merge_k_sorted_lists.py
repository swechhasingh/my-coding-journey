import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val
        
def merge_k_sorted_lists(lists):
    min_heap = []
    # create min heap with smallest elements from each list to find the smallest element for merged list
    for sorted_list in lists:
        if sorted_list:
            heapq.heappush(min_heap, sorted_list)

    merged_list_head = None
    merged_list_tail = None
    # while the minheap has element, pop the minimum element from heap and add it to the final merged list
    # push the next element in min heap from the list to which the poped element belongs
    while min_heap:
        curr_heap_min = heapq.heappop(min_heap)
        if merged_list_head is None:
            merged_list_head, merged_list_tail = curr_heap_min, curr_heap_min
        else:
            merged_list_tail.next = curr_heap_min
            merged_list_tail = merged_list_tail.next
        if curr_heap_min.next:
            heapq.heappush(min_heap, curr_heap_min.next)
        
    return merged_list_head

def main():
    # 2,6,8
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)
    # 3,6,8
    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)
    #1,3,4
    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)
    #1,2,3,3,4,6,6,8
    result = merge_k_sorted_lists([l1, l2, l3])
    print("Merged list: ", end='')
    while result is not None:
        print(f"{result.val} ", end='')
        result = result.next
    print()


main()