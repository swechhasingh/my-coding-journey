class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head, p, q):
    # Time complexity: O(N)
    # Space complexity: O(1)
    if head is None:
        return head

    count = 1
    # find p
    curr = head
    left = head
    while count != p:
        left = curr
        curr = curr.next
        count += 1
    # p: start of sub-list
    start = curr

    # find q
    while count != q:
        curr = curr.next
        count += 1
    # q: end of sub-list
    end = curr
    right = end.next

    # reverse sub-list
    prev = right
    curr = start
    while curr != right:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    if p == 1:
        head = prev
    else:
        left.next = prev
    
    return head

def print_linked_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"Original linked list: ",end="")
    print_linked_list(head)
    print(f"Reversed linked list: ",end="")
    print_linked_list(reverse_linked_list(head,1,4))

main()