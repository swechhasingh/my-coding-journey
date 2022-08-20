class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.visited = 0

def start_of_cycle(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    slow, fast = head, head
    slow.visited = 1
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        slow.visited = 1
        if slow == fast:
            slow = slow.next
            while slow != fast:
                if slow.visited == 1:
                    return slow.val
                slow.visited = 1
                slow = slow.next
    return None


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(start_of_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(start_of_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(start_of_cycle(head)))


main()