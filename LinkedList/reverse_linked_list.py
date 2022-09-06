class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    if head is None:
        return head
    prev = head
    curr = head.next
    head.next = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

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
    print_linked_list(reverse_linked_list(head))

main()