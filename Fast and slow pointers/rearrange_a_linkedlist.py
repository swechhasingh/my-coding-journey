class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def rearrange_linkedlist(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    if head is None or head.next is None:
        return 

    # find the middle of linkedlist
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    print(f"Middle of linkedlist: {slow.val}")
    # reverse the second half of linkedlist
    tail = reverse_linkedlist(slow)

    print("First half of the linkedlist:", end=" ")
    print_linked_list(head)
    print("Reversed second half of the linkedlist:", end=" ")
    print_linked_list(tail)

    left, right = head, tail
    while left is not None and right is not None and left.next != right:
        left_next = left.next
        right_next = right.next
        left.next = right
        right.next = left_next
        left = left_next
        right = right_next
    
    print("Rearranged linkedlist:", end=" ")
    print_linked_list(head)

    return

def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

def reverse_linkedlist(head):
    prev = None
    curr= head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # return tail of the linkedlist
    return prev

    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Original linkedlist: ", end=" ")
    print_linked_list(head)
    rearrange_linkedlist(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    print("Original linkedlist: ", end=" ")
    print_linked_list(head)
    rearrange_linkedlist(head)

main()