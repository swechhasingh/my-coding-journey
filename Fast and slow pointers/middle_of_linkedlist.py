class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def middle_of_linkedlist(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    if head is None:
        return None
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Middle of LinkedList(odd length): " + str(middle_of_linkedlist(head)))

    head.next.next.next.next.next = Node(6)
    print("Middle of LinkedList(even length): " + str(middle_of_linkedlist(head)))

main()