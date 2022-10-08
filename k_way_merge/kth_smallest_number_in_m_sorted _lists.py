import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val
        
def merge_k_sorted_lists(lists,k):
    min_heap = []
    # create min heap with smallest elements from each list to find the smallest element for merged list
    for sorted_list in lists:
        if sorted_list:
            heapq.heappush(min_heap, sorted_list)

    count = 0 
    while min_heap:
        curr_heap_min = heapq.heappop(min_heap)
        count += 1
        if count == k:
            return curr_heap_min.val
        if curr_heap_min.next:
            heapq.heappush(min_heap, curr_heap_min.next)
        
    return -1

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
    #1,2,3,3,4,6,6,7,8
    result = merge_k_sorted_lists([l1, l2, l3],5)
    print("k-th samllest number in merged list: ", result)
    


main()